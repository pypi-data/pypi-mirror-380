"""
NodeContext for explicit streaming event emission from PocketFlow nodes.

This module provides a clean, simple approach where nodes are directly responsible
for emitting their own streaming events through an injected NodeContext object.
"""

import uuid
from typing import Dict, Any, List, Optional

from .ai_sdk_events import (
    AiSdkEvent,
    ToolInputStartEvent,
    ToolInputDeltaEvent,
    ToolInputAvailableEvent,
    ToolOutputAvailableEvent,
    TextStartEvent,
    TextDeltaEvent,
    TextEndEvent,
)


class NodeContext:
    """
    Context object for nodes to emit streaming events.

    Each node receives a fresh NodeContext instance during streaming execution.
    Nodes can emit various types of AI-SDK compatible events directly.
    """

    def __init__(self):
        """Initialize a new node context with an empty event queue."""
        self._events: List[AiSdkEvent] = []

    # Tool Events
    def emit_tool_start(self, tool_call_id: str, tool_name: str):
        """Emit tool input start event."""
        event = ToolInputStartEvent(tool_call_id, tool_name)
        self._events.append(event)

    def emit_tool_delta(self, tool_call_id: str, input_delta: str):
        """Emit tool input delta event (streaming arguments)."""
        event = ToolInputDeltaEvent(tool_call_id, input_delta)
        self._events.append(event)

    def emit_tool_available(
        self, tool_call_id: str, tool_name: str, input_data: Dict[str, Any]
    ):
        """Emit tool input available event (complete arguments)."""
        event = ToolInputAvailableEvent(tool_call_id, tool_name, input_data)
        self._events.append(event)

    def emit_tool_output(
        self, tool_call_id: str, output: Dict[str, Any], preliminary: bool = False
    ):
        """Emit tool output event (status, result, etc.)."""
        event = ToolOutputAvailableEvent(tool_call_id, output, preliminary)
        self._events.append(event)

    # Text Events
    def emit_text_start(self, text_id: Optional[str] = None) -> str:
        """
        Emit text start event and return text ID for subsequent deltas.

        Args:
            text_id: Optional text ID, will generate one if not provided

        Returns:
            The text ID to use for subsequent text_delta calls
        """
        if text_id is None:
            text_id = f"txt-{str(uuid.uuid4())[:8]}"

        event = TextStartEvent(text_id)
        self._events.append(event)
        return text_id

    def emit_text_delta(self, text_id: str, delta: str):
        """Emit text delta event (streaming content)."""
        event = TextDeltaEvent(text_id, delta)
        self._events.append(event)

    def emit_text_end(self, text_id: str):
        """Emit text end event."""
        event = TextEndEvent(text_id)
        self._events.append(event)

    # Custom Events
    def emit_custom(self, event_type: str, data: Dict[str, Any]):
        """Emit a custom event with arbitrary data."""
        event = AiSdkEvent(event_type, data)
        self._events.append(event)

    # Convenience Methods
    def emit_tool_execution(
        self, tool_call_id: str, tool_name: str, tool_args: Dict[str, Any], result: Any
    ):
        """
        Convenience method to emit a complete tool execution sequence.

        Emits: tool-start -> tool-available -> tool-output (loading) -> tool-output (success)
        """
        # Start
        self.emit_tool_start(tool_call_id, tool_name)

        # Arguments available
        self.emit_tool_available(tool_call_id, tool_name, tool_args)

        # Loading status
        self.emit_tool_output(
            tool_call_id,
            {"status": "loading", "text": f"Executing {tool_name}..."},
            preliminary=True,
        )

        # Success result
        self.emit_tool_output(
            tool_call_id,
            {
                "status": "success",
                "text": f"Tool {tool_name} completed successfully",
                "result": result,
            },
        )

    def emit_tool_error(self, tool_call_id: str, tool_name: str, error: str):
        """Convenience method to emit tool error."""
        self.emit_tool_output(
            tool_call_id,
            {
                "status": "error",
                "text": f"Tool {tool_name} failed: {error}",
                "error": error,
            },
        )

    def emit_text_stream(self, content_chunks: List[str]) -> str:
        """
        Convenience method to emit a complete text stream.

        Args:
            content_chunks: List of text chunks to stream

        Returns:
            The text ID used for the stream
        """
        text_id = self.emit_text_start()

        for chunk in content_chunks:
            self.emit_text_delta(text_id, chunk)

        self.emit_text_end(text_id)
        return text_id

    # Event Retrieval
    def get_events(self) -> List[AiSdkEvent]:
        """Get all events and clear the queue."""
        events = self._events.copy()
        self._events.clear()
        return events

    def has_events(self) -> bool:
        """Check if there are events in the queue."""
        return len(self._events) > 0

    def event_count(self) -> int:
        """Get the number of events in the queue."""
        return len(self._events)

    def peek_events(self) -> List[AiSdkEvent]:
        """Get all events without clearing the queue."""
        return self._events.copy()

    # One-Liner Convenience Methods
    def stream_llm_response(self, stream_response):
        """
        ONE-LINER: Automatically stream an LLM response.

        Detects whether the response contains tool calls or content and
        emits the appropriate streaming events automatically.

        Args:
            stream_response: StreamResponse object from call_llm_stream()
        """
        import json

        # Check for tool calls first
        tool_calls = stream_response.tool_calls()

        if tool_calls:
            # LLMNode doesn't emit tool events - that's ToolNode's responsibility
            # Just handle the tool call detection for routing
            pass
        else:
            # Stream content using actual LLM streaming events
            if hasattr(stream_response, "event_stream") and stream_response.event_stream:
                # Use actual streaming events from LLM
                text_id = None
                for event in stream_response.event_stream:
                    if hasattr(event, 'event_type') and event.event_type.value == 'assistant_response':
                        # Start text stream on first event
                        if text_id is None:
                            text_id = self.emit_text_start()

                        # Emit delta for each chunk
                        if hasattr(event, 'content') and event.content:
                            self.emit_text_delta(text_id, event.content)

                # End text stream
                if text_id is not None:
                    self.emit_text_end(text_id)
            elif hasattr(stream_response, "content") and stream_response.content:
                # Fallback: use complete content as single chunk
                text_id = self.emit_text_start()
                self.emit_text_delta(text_id, stream_response.content)
                self.emit_text_end(text_id)


    def stream_tool_input_events(self, messages):
        """
        Emit tool input events for pending tool calls.

        This includes: tool-input-start, tool-input-delta, tool-input-available

        Args:
            messages: Messages object containing pending tool calls
        """
        import json

        pending_calls = messages.get_pending_tool_calls()
        for tool_call in pending_calls:
            tool_call_id = tool_call["tool_call_id"]
            tool_name = tool_call["tool_name"]
            tool_args = tool_call["arguments"]

            # Emit tool input events
            self.emit_tool_start(tool_call_id, tool_name)

            # Generate delta events for arguments
            args_json = json.dumps(tool_args, separators=(",", ":"))
            if args_json and args_json != "{}":
                self.emit_tool_delta(tool_call_id, args_json)

            self.emit_tool_available(tool_call_id, tool_name, tool_args)

    def stream_tool_loading(self, messages):
        """
        Emit loading events for pending tool calls.

        Should be called BEFORE execute_pending_tool_calls.

        Args:
            messages: Messages object containing pending tool calls
        """
        pending_calls = messages.get_pending_tool_calls()
        for tool_call in pending_calls:
            tool_call_id = tool_call["tool_call_id"]
            tool_name = tool_call["tool_name"]

            # Emit loading state
            self.emit_tool_output(
                tool_call_id,
                {
                    "status": "loading",
                    "text": f"Executing {tool_name}...",
                },
                preliminary=True
            )

    def stream_tool_execution(self, tool_responses):
        """
        ONE-LINER: Automatically stream tool execution results.

        Takes tool responses from execute_pending_tool_calls() and
        emits appropriate execution streaming events.

        Args:
            tool_responses: List of tool response objects from execute_pending_tool_calls()
        """
        for response in tool_responses:
            tool_call_id = response.get("tool_call_id")
            if tool_call_id:
                is_error = response.get("is_error", False)

                if is_error:
                    # Emit error completion
                    self.emit_tool_output(
                        tool_call_id,
                        {
                            "status": "error",
                            "text": f"Tool execution failed: {response.get('error', 'Unknown error')}",
                            "error": response.get("error"),
                        },
                        preliminary=False
                    )
                else:
                    # Emit success completion
                    self.emit_tool_output(
                        tool_call_id,
                        {
                            "status": "success",
                            "text": "Tool execution completed",
                            "result": response.get("tool_response"),
                        },
                        preliminary=False
                    )
