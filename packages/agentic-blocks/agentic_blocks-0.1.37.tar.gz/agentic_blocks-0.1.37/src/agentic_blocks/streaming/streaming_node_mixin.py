"""
StreamingNodeMixin for PocketFlow nodes to support streaming event emission.

This mixin provides the interface for nodes to receive and use a NodeContext
for emitting streaming events during execution.
"""

from typing import Optional
from .node_context import NodeContext


class StreamingNodeMixin:
    """
    Mixin class that provides streaming context support for PocketFlow nodes.

    Nodes can inherit from both their base Node class and this mixin to gain
    streaming capabilities. The context is injected by the StreamingFlow wrapper.

    Example:
        class MyLLMNode(Node, StreamingNodeMixin):
            def exec(self, inputs):
                if self.has_context():
                    self.context.emit_text_start()
                    # ... emit events during processing
                return result
    """

    def __init__(self, *args, **kwargs):
        """Initialize the mixin with no context."""
        super().__init__(*args, **kwargs)
        self.context: Optional[NodeContext] = None

    def set_context(self, context: NodeContext):
        """
        Set the streaming context for this node.

        This method is called by StreamingFlow before node execution.

        Args:
            context: NodeContext instance for event emission
        """
        self.context = context

    def has_context(self) -> bool:
        """
        Check if this node has a streaming context available.

        Returns:
            True if context is available for event emission
        """
        return self.context is not None

    def clear_context(self):
        """Clear the streaming context (useful for cleanup)."""
        self.context = None

    # ONE-LINER Streaming Methods
    def stream_llm_response(self, stream_response):
        """
        ONE-LINER: Automatically stream an LLM response.

        Usage:
            stream_response = call_llm_stream(messages.get_messages(), tools=tools)
            self.stream_llm_response(stream_response)

        Args:
            stream_response: StreamResponse object from call_llm_stream()
        """
        if self.has_context():
            self.context.stream_llm_response(stream_response)

    def stream_tool_input_events(self, messages):
        """
        ONE-LINER: Stream tool input events for pending tool calls.

        This includes: tool-input-start, tool-input-delta, tool-input-available

        Usage:
            self.stream_tool_input_events(messages)     # Emit input events
            self.stream_tool_loading(messages)          # Emit loading events
            tool_responses = execute_pending_tool_calls(messages, tool_registry)
            self.stream_tool_execution(tool_responses)  # Emit completion events

        Args:
            messages: Messages object containing pending tool calls
        """
        if self.has_context():
            self.context.stream_tool_input_events(messages)

    def stream_tool_loading(self, messages):
        """
        ONE-LINER: Stream loading states for pending tool calls.

        Usage:
            self.stream_tool_input_events(messages)     # Emit input events
            self.stream_tool_loading(messages)          # Emit loading events
            tool_responses = execute_pending_tool_calls(messages, tool_registry)
            self.stream_tool_execution(tool_responses)  # Emit completion events

        Args:
            messages: Messages object containing pending tool calls
        """
        if self.has_context():
            self.context.stream_tool_loading(messages)


    def stream_tool_execution(self, tool_responses):
        """
        ONE-LINER: Automatically stream tool execution results.

        Usage:
            self.stream_tool_loading(messages)  # Before execute_pending_tool_calls
            tool_responses = execute_pending_tool_calls(messages, tool_registry)
            self.stream_tool_execution(tool_responses)  # After execute_pending_tool_calls

        Args:
            tool_responses: List of tool response objects from execute_pending_tool_calls()
        """
        if self.has_context():
            self.context.stream_tool_execution(tool_responses)