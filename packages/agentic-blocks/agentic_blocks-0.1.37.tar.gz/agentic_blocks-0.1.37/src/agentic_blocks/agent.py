import asyncio
import json
import logging
import time
import threading
import hashlib
import signal
import os
from typing import AsyncIterator, List, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import StreamingResponse
from pocketflow import Node, Flow

from agentic_blocks.llm_agno import call_llm_stream
from agentic_blocks.utils.tools_utils import (
    create_tool_registry,
    execute_pending_tool_calls,
    agno_tools_to_openai_format,
)
from agentic_blocks.messages import Messages
from agentic_blocks.streaming import StreamingNodeMixin, StreamingFlow
from agentic_blocks.models import ChatRequest
from agentic_blocks.utils.server_utils import extract_message_content


class AgentServerState:
    """Thread-safe container for the current agent instance."""

    def __init__(self, agent: 'Agent'):
        self.agent = agent
        self._lock = threading.Lock()

    def get_current_agent(self) -> 'Agent':
        """Get the current agent instance (thread-safe)."""
        with self._lock:
            return self.agent

    def update_agent(self, new_agent: 'Agent'):
        """Update the current agent instance (thread-safe)."""
        with self._lock:
            self.agent = new_agent


class AgentWatcher:
    """Background thread that monitors agent configuration changes and triggers hot-reloads."""

    def __init__(self, agent_to_watch: 'Agent', server_state: AgentServerState, check_interval: float = 1.5):
        self.agent_to_watch = agent_to_watch  # Live reference to the agent being modified
        self.server_state = server_state
        self.check_interval = check_interval
        self.last_config_hash = agent_to_watch._compute_config_hash()
        self._stop_event = threading.Event()
        self._watcher_thread = None
        self._is_running = False

    def start_watching(self):
        """Start the background watcher thread."""
        if self._watcher_thread and self._watcher_thread.is_alive():
            return

        self._stop_event.clear()
        self._watcher_thread = threading.Thread(target=self._watch_loop, daemon=True)
        self._watcher_thread.start()
        self._is_running = True
        print("👁️  Started automatic config monitoring")

    def stop_watching(self):
        """Stop the background watcher thread."""
        if not self._is_running:
            return

        self._stop_event.set()
        if self._watcher_thread:
            self._watcher_thread.join(timeout=3.0)
        self._is_running = False
        print("🛑 Stopped automatic config monitoring")

    def _watch_loop(self):
        """Main watching loop that runs in background thread."""
        while not self._stop_event.is_set():
            try:
                # Monitor the live agent instance that users are modifying
                current_hash = self.agent_to_watch._compute_config_hash()
                if current_hash != self.last_config_hash:
                    print("🔄 Agent configuration changed - hot-reloading...")
                    print(f"   Previous hash: {self.last_config_hash[:8]}...")
                    print(f"   Current hash:  {current_hash[:8]}...")
                    print(f"   System prompt: '{self.agent_to_watch.system_prompt[:50]}{'...' if len(self.agent_to_watch.system_prompt) > 50 else ''}'")
                    print(f"   Tools count: {len(self.agent_to_watch.tools)}")

                    # Create new agent with the CURRENT configuration from the live agent
                    new_agent = Agent(
                        system_prompt=self.agent_to_watch.system_prompt,
                        tools=self.agent_to_watch.tools
                    )

                    # Update the server state with the new agent
                    self.server_state.update_agent(new_agent)
                    self.last_config_hash = current_hash
                    print("✅ Agent hot-reloaded successfully")

                # Wait for next check
                if not self._stop_event.wait(self.check_interval):
                    continue
                else:
                    break

            except Exception as e:
                print(f"⚠️ Error in config watcher: {e}")
                if not self._stop_event.wait(self.check_interval):
                    continue
                else:
                    break

    def check_for_changes(self):
        """Manually trigger a change check (useful for debugging)."""
        if not self._is_running:
            print("❌ Watcher is not running")
            return

        current_hash = self.agent_to_watch._compute_config_hash()
        print(f"🔍 Manual change check:")
        print(f"   Last hash:    {self.last_config_hash[:8]}...")
        print(f"   Current hash: {current_hash[:8]}...")
        print(f"   Changed: {'Yes' if current_hash != self.last_config_hash else 'No'}")

        if current_hash != self.last_config_hash:
            print("🔄 Configuration changed - triggering reload...")
            self.last_config_hash = current_hash
            return True
        return False


class Agent:
    """Modern Agent with streaming capabilities"""

    # Class-level registry to track active servers
    _active_servers = {}  # port -> (server_state, watcher, thread)

    def __init__(self, system_prompt: str, tools: list):
        self.system_prompt = system_prompt
        self.tools = tools
        self.tool_registry = create_tool_registry(tools)
        self.openai_tools = agno_tools_to_openai_format(tools)
        self.flow = self._create_flow()
        self._config_hash = self._compute_config_hash()

        # New hot-reloading infrastructure
        self._server_state = None
        self._agent_watcher = None
        self._server_thread = None
        self._server_port = None

    def _create_flow(self) -> Flow:
        """Create the agent flow with streaming nodes"""

        class LLMNode(Node, StreamingNodeMixin):
            def __init__(self, system_prompt, openai_tools):
                super().__init__()
                self.system_prompt = system_prompt
                self.openai_tools = openai_tools

            def prep(self, shared):
                return shared["messages"]

            def exec(self, messages: Messages) -> tuple[Messages, object]:
                stream_response = call_llm_stream(messages.get_messages(), tools=self.openai_tools)

                if stream_response.tool_calls():
                    self.stream_llm_response(stream_response)
                    messages.add_tool_calls(stream_response.tool_calls())
                else:
                    messages.add_assistant_message(stream_response.content)

                return messages, stream_response

            def post(self, shared, prep_res, exec_res):
                shared["messages"], shared["stream_response"] = exec_res
                return "use_tool" if shared["messages"].has_pending_tool_calls() else "answer_node"

        class ToolNode(Node, StreamingNodeMixin):
            def __init__(self, tool_registry):
                super().__init__()
                self.tool_registry = tool_registry

            def prep(self, shared):
                return shared["messages"]

            def exec(self, messages: Messages) -> Messages:
                # Stream tool input events (start, delta, available)
                self.stream_tool_input_events(messages)

                # Stream loading state BEFORE execution
                self.stream_tool_loading(messages)

                # Execute tools (separate from streaming)
                tool_responses = execute_pending_tool_calls(messages, self.tool_registry)

                # Stream completion AFTER execution
                self.stream_tool_execution(tool_responses)

                # Add responses to messages
                messages.add_tool_responses(tool_responses)
                return messages

            def post(self, shared, prep_res, messages):
                return "llm_node"

        class AnswerNode(Node, StreamingNodeMixin):
            def prep(self, shared):
                self.stream_llm_response(shared["stream_response"])

                messages = shared["messages"]
                shared["answer"] = messages.get_messages()[-1]
                return messages

            def exec(self, messages):
                return messages

        # Create nodes
        llm_node = LLMNode(self.system_prompt, self.openai_tools)
        tool_node = ToolNode(self.tool_registry)
        answer_node = AnswerNode()

        # Set up flow routing
        llm_node - "use_tool" >> tool_node
        tool_node - "llm_node" >> llm_node
        llm_node - "answer_node" >> answer_node

        return Flow(start=llm_node)

    async def run_stream_sse(self, user_prompt: str) -> AsyncIterator[str]:
        """Run the agent and stream SSE events"""
        # Create messages
        messages = Messages(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt
        )

        shared = {"messages": messages}

        # Stream the flow execution
        wrapper = StreamingFlow(self.flow)
        async for sse_event in wrapper.run_stream_sse(shared):
            yield sse_event

    def _compute_config_hash(self) -> str:
        """Compute a hash of the agent's configuration for change detection."""
        # Create a string representation of the agent's key configuration
        tool_names = []
        for tool in self.tools:
            if hasattr(tool, '__name__'):
                tool_names.append(tool.__name__)
            elif hasattr(tool, 'name'):
                tool_names.append(tool.name)
            else:
                tool_names.append(str(tool))

        config_str = f"{self.system_prompt}|{len(self.tools)}|{sorted(tool_names)}"
        return hashlib.md5(config_str.encode()).hexdigest()

    def _is_running_in_notebook(self) -> bool:
        """Detect if we're running in a Jupyter notebook environment."""
        try:
            # Check for IPython and if we're in a notebook kernel
            from IPython import get_ipython
            ipython = get_ipython()

            if ipython is None:
                return False

            # Check if we're in a notebook kernel (not just IPython shell)
            return hasattr(ipython, 'kernel')

        except ImportError:
            # IPython not available
            return False

    def stop_server(self):
        """
        Stop the server and all associated monitoring threads.

        This provides a clean shutdown without killing processes.
        """
        stopped_components = []

        # Stop the background watcher
        if self._agent_watcher:
            self._agent_watcher.stop_watching()
            stopped_components.append("config watcher")

        # Note about server thread
        if self._server_thread and self._server_thread.is_alive():
            stopped_components.append("server monitoring")
            print(f"🛑 Stopped {', '.join(stopped_components)}")
            print("💡 Note: The uvicorn server will continue running in the background")
            print("💡 In notebooks, restart the kernel to fully stop all servers")

            # Unregister from class-level registry
            if self._server_port:
                self._unregister_server(self._server_port)

            # Clean up references
            self._server_thread = None
            self._server_port = None
            self._server_state = None
            self._agent_watcher = None
        else:
            print("❌ No server components are currently running")

    def server_status(self):
        """Get the current status of the server and hot-reloading components."""
        if not self._server_thread:
            print("❌ No server started")
            return

        server_running = self._server_thread.is_alive() if self._server_thread else False
        watcher_running = self._agent_watcher._is_running if self._agent_watcher else False

        print(f"🚀 Server: {'🟢 Running' if server_running else '🔴 Stopped'}")
        if self._server_port:
            print(f"🌐 URL: http://0.0.0.0:{self._server_port}")
        print(f"👁️  Hot-reloading: {'🟢 Active' if watcher_running else '🔴 Inactive'}")

        if self._server_state:
            current_agent = self._server_state.get_current_agent()
            print(f"⚙️  Config hash: {current_agent._compute_config_hash()}")

        return {
            "server_running": server_running,
            "hot_reloading": watcher_running,
            "port": self._server_port,
            "config_hash": self._compute_config_hash()
        }

    def check_config_changes(self):
        """Manually trigger a configuration change check (useful for debugging)."""
        if not self._agent_watcher:
            print("❌ No hot-reloading watcher available")
            return

        return self._agent_watcher.check_for_changes()

    def take_over_server(self, port: int = 8000):
        """
        Take over an existing server running on the specified port with this agent instance.

        This is useful when you create a new agent instance and want it to replace
        the agent in an already-running server.

        Args:
            port: The port of the server to take over

        Returns:
            True if takeover was successful, False if no server found on that port
        """
        if port in Agent._active_servers:
            server_state, watcher, thread = Agent._active_servers[port]

            print(f"🔄 Taking over server on port {port} with new agent...")

            # Update the server state with this new agent
            server_state.update_agent(self)

            # Update the watcher to monitor this new agent
            watcher.agent_to_watch = self
            watcher.last_config_hash = self._compute_config_hash()

            # Update this agent's references
            self._server_state = server_state
            self._agent_watcher = watcher
            self._server_thread = thread
            self._server_port = port

            print("✅ Server takeover successful - new agent is now active")
            return self._server_thread
        else:
            print(f"❌ No active server found on port {port}")
            return None

    @classmethod
    def list_active_servers(cls):
        """List all active servers managed by Agent instances."""
        if not cls._active_servers:
            print("❌ No active servers")
            return

        print("🚀 Active Agent Servers:")
        for port, (server_state, watcher, thread) in cls._active_servers.items():
            current_agent = server_state.get_current_agent()
            status = "🟢 Running" if thread.is_alive() else "🔴 Stopped"
            hot_reload = "🟢 Active" if watcher._is_running else "🔴 Inactive"

            print(f"   Port {port}: {status}, Hot-reload: {hot_reload}")
            print(f"      System prompt: '{current_agent.system_prompt[:40]}{'...' if len(current_agent.system_prompt) > 40 else ''}'")
            print(f"      Tools: {len(current_agent.tools)} tools")

    def _register_server(self, port: int):
        """Register this agent's server in the class-level registry."""
        Agent._active_servers[port] = (self._server_state, self._agent_watcher, self._server_thread)

    def _unregister_server(self, port: int):
        """Unregister server from the class-level registry."""
        if port in Agent._active_servers:
            del Agent._active_servers[port]

    async def _generate_ui_message_stream(self, request: ChatRequest):
        """Generate streaming response using Agent class."""
        logger = logging.getLogger(__name__)
        logger.info(f"Starting chat - {len(request.messages)} messages")

        try:
            # Extract the latest user message
            user_message = ""
            for ui_msg in reversed(request.messages):
                if ui_msg.role == "user":
                    user_message = extract_message_content(ui_msg)
                    break

            if not user_message:
                user_message = "Hello"

            # Stream response using agent
            async for sse_event in self.run_stream_sse(user_message):
                yield sse_event
                # Force flush to prevent buffering
                await asyncio.sleep(0.01)

            logger.info("Chat completed")

        except Exception as e:
            logger.error(f"Error in chat stream: {str(e)}", exc_info=True)
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"

    def serve(self, host: str = "0.0.0.0", port: int = 8000, allowed_origins: Optional[List[str]] = None, debug: bool = False, background: Optional[bool] = None, reload: bool = True):
        """
        Serve the agent as a FastAPI web service with automatic hot-reloading.

        Args:
            host: Host to bind to (default: "0.0.0.0")
            port: Port to bind to (default: 8000)
            allowed_origins: CORS allowed origins (default: ["*"])
            debug: Enable debug logging (default: False)
            background: Run server in background thread, useful for notebooks.
                       If None (default), auto-detects notebook environment.
            reload: Enable automatic hot-reloading (default: True)

        Returns:
            If background=True, returns a threading.Thread object that can be used to stop the server
        """
        if allowed_origins is None:
            allowed_origins = ["*"]

        # Auto-detect notebook environment if background not explicitly set
        if background is None:
            background = self._is_running_in_notebook()
            if background:
                print("📓 Detected Jupyter notebook environment - starting server in background")

        # Check if this agent already has a server running
        if self._server_thread and self._server_thread.is_alive():
            print(f"✅ Server already running at http://{host}:{self._server_port}")
            if reload and not self._agent_watcher._is_running:
                self._agent_watcher.start_watching()
            return self._server_thread

        # Check if there's an existing server on this port (from another agent)
        if port in Agent._active_servers:
            print(f"🔍 Found existing server on port {port}")
            print("💡 Auto-taking over existing server with new agent...")
            return self.take_over_server(port)

        # Initialize shared state and watcher for hot-reloading
        if reload:
            if not self._server_state:
                self._server_state = AgentServerState(self)
            if not self._agent_watcher:
                self._agent_watcher = AgentWatcher(self, self._server_state)

        def get_current_agent():
            """FastAPI dependency to get the current agent instance."""
            if self._server_state:
                return self._server_state.get_current_agent()
            return self

        def _create_app():
            # Setup logging
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            logger = logging.getLogger(__name__)

            app = FastAPI(title="Agentic Blocks Agent API")
            app.add_middleware(
                CORSMiddleware,
                allow_origins=allowed_origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
            )

            @app.exception_handler(RequestValidationError)
            async def validation_exception_handler(_: Request, exc: RequestValidationError):
                logger.error(f"Validation error: {exc.errors()}")
                return HTTPException(status_code=422, detail=f"Validation error: {exc.errors()}")

            @app.post("/chat")
            async def chat_endpoint(request: ChatRequest):
                """Chat endpoint compatible with AI SDK useChat hook."""
                logger.info(f"Chat request: {request.model}, {len(request.messages)} messages")

                # Get current agent (hot-reloadable)
                current_agent = get_current_agent()

                # Validate API key
                try:
                    from agentic_blocks.utils.config_utils import get_llm_config
                    config = get_llm_config()
                    if not config.get("api_key"):
                        raise HTTPException(status_code=500, detail="API key not configured. Set OPENROUTER_API_KEY or OPENAI_API_KEY.")
                except ValueError as e:
                    raise HTTPException(status_code=500, detail=str(e))

                return StreamingResponse(
                    current_agent._generate_ui_message_stream(request),
                    media_type="text/plain; charset=utf-8",
                    headers={
                        "x-vercel-ai-ui-message-stream": "v1",
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive"
                    }
                )

            @app.get("/health")
            async def health_check():
                """Health check endpoint."""
                try:
                    from agentic_blocks.utils.config_utils import get_llm_config
                    api_key_configured = bool(get_llm_config().get("api_key"))
                except (ValueError, ImportError):
                    api_key_configured = False

                current_agent = get_current_agent()
                return {
                    "status": "healthy",
                    "timestamp": time.time(),
                    "api_key_configured": api_key_configured,
                    "hot_reloading": reload and self._agent_watcher._is_running if self._agent_watcher else False,
                    "agent_config_hash": current_agent._compute_config_hash()
                }

            @app.get("/")
            async def root():
                """Root endpoint."""
                return {"message": "Agentic Blocks Agent API", "version": "1.0.0"}

            return app

        def _run_server():
            """Run the server in a separate thread."""
            import uvicorn
            logger = logging.getLogger(__name__)
            logger.info(f"Starting server at http://{host}:{port}")

            app = _create_app()
            uvicorn.run(app, host=host, port=port, log_level="info" if debug else "warning")

        # Start the server
        if background:
            # Run server in background thread (useful for notebooks)
            server_thread = threading.Thread(target=_run_server, daemon=True)
            server_thread.start()
            self._server_thread = server_thread
            self._server_port = port

            # Start hot-reloading watcher
            if reload:
                self._agent_watcher.start_watching()

            # Register server in class-level registry
            self._register_server(port)

            print(f"🚀 Server started in background at http://{host}:{port}")
            print("💡 Use this in notebooks to avoid blocking the cell")
            print("🛑 Use agent.stop_server() to stop the server")
            return server_thread
        else:
            # Run server in current thread (blocks execution)
            self._server_port = port

            # Start hot-reloading watcher in background even for foreground server
            if reload:
                self._agent_watcher.start_watching()

            # Register server in class-level registry (for foreground servers too)
            self._register_server(port)

            _run_server()