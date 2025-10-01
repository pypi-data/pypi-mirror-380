"""
Simplified streaming flow wrapper using NodeContext injection.

This module provides a clean streaming approach where each node receives
a fresh NodeContext and is responsible for emitting its own events.
"""

import copy
from typing import Any, AsyncIterator, Dict, Union

from .ai_sdk_events import (
    AiSdkEvent,
    AiSdkEventType,
    StreamEventTransformer,
    format_ai_sdk_sse_event,
    create_done_event,
)
from .node_context import NodeContext
from .streaming_node_mixin import StreamingNodeMixin


class StreamingFlow:
    """
    Clean streaming flow wrapper using NodeContext injection.

    This approach gives each node a fresh NodeContext instance and allows
    nodes to explicitly emit their own events during execution.
    """

    def __init__(self, flow: Any):
        """
        Initialize streaming wrapper for a PocketFlow Flow.

        Args:
            flow: PocketFlow Flow instance to wrap
        """
        self.flow = flow
        self.transformer = StreamEventTransformer()

    async def run_stream(self, shared: Dict[str, Any]) -> AsyncIterator[AiSdkEvent]:
        """
        Execute the flow with real-time AI-SDK compatible streaming events.

        Args:
            shared: Shared state dictionary for the flow

        Yields:
            AiSdkEvent objects in AI-SDK compatible format as they occur
        """
        # Emit flow start
        yield self.transformer.create_flow_start()

        try:
            # Execute flow with NodeContext injection
            async for event in self._execute_flow_with_contexts(shared):
                yield event

        except Exception as e:
            # Emit error event
            error_event = AiSdkEvent(AiSdkEventType.ERROR, {
                "error": str(e),
                "type": type(e).__name__
            })
            yield error_event

        # Emit flow finish
        yield self.transformer.create_flow_finish()

    async def _execute_flow_with_contexts(
        self,
        shared: Dict[str, Any]
    ) -> AsyncIterator[AiSdkEvent]:
        """
        Execute the flow while injecting NodeContext into each node.

        Args:
            shared: Shared state dictionary

        Yields:
            AiSdkEvent objects as they occur during execution
        """
        # Copy the flow parameters
        params = {**self.flow.params} if hasattr(self.flow, 'params') else {}
        curr_node = copy.copy(self.flow.start_node)
        last_action = None

        # Execute flow orchestration
        while curr_node:
            # Emit step start
            step_start_event = self.transformer.create_step_start()
            yield step_start_event

            # Set node parameters
            if hasattr(curr_node, 'set_params'):
                curr_node.set_params(params)

            # Create fresh NodeContext for this node
            node_context = NodeContext()

            # Inject context if node supports it
            if isinstance(curr_node, StreamingNodeMixin):
                curr_node.set_context(node_context)

            # Execute node
            last_action = curr_node._run(shared)

            # Emit events that were collected during node execution
            node_events = node_context.get_events()
            for event in node_events:
                yield event

            # Clean up context
            if isinstance(curr_node, StreamingNodeMixin):
                curr_node.clear_context()

            # Emit step finish
            step_finish_event = self.transformer.create_step_finish()
            yield step_finish_event

            # Get next node
            curr_node = copy.copy(self.flow.get_next_node(curr_node, last_action))

    async def run_stream_sse(self, shared: Dict[str, Any]) -> AsyncIterator[str]:
        """
        Execute the flow with Server-Sent Events (SSE) formatted output.

        Args:
            shared: Shared state dictionary for the flow

        Yields:
            SSE-formatted strings ready for FastAPI streaming
        """
        async for event in self.run_stream(shared):
            yield format_ai_sdk_sse_event(event)

        # Final DONE event
        yield create_done_event()


class AsyncStreamingFlow:
    """
    Async version of the simplified streaming flow wrapper.
    """

    def __init__(self, async_flow: Any):
        """
        Initialize async streaming wrapper for a PocketFlow AsyncFlow.

        Args:
            async_flow: PocketFlow AsyncFlow instance to wrap
        """
        self.flow = async_flow
        self.transformer = StreamEventTransformer()

    async def run_stream(self, shared: Dict[str, Any]) -> AsyncIterator[AiSdkEvent]:
        """
        Execute the async flow with real-time AI-SDK compatible streaming events.

        Args:
            shared: Shared state dictionary for the flow

        Yields:
            AiSdkEvent objects in AI-SDK compatible format as they occur
        """
        # Emit flow start
        yield self.transformer.create_flow_start()

        try:
            # Execute flow with NodeContext injection
            async for event in self._execute_async_flow_with_contexts(shared):
                yield event

        except Exception as e:
            # Emit error event
            error_event = AiSdkEvent(AiSdkEventType.ERROR, {
                "error": str(e),
                "type": type(e).__name__
            })
            yield error_event

        # Emit flow finish
        yield self.transformer.create_flow_finish()

    async def _execute_async_flow_with_contexts(
        self,
        shared: Dict[str, Any]
    ) -> AsyncIterator[AiSdkEvent]:
        """
        Execute the async flow while injecting NodeContext into each node.

        Args:
            shared: Shared state dictionary

        Yields:
            AiSdkEvent objects as they occur during execution
        """
        # Copy the flow parameters
        params = {**self.flow.params} if hasattr(self.flow, 'params') else {}
        curr_node = copy.copy(self.flow.start_node)
        last_action = None

        # Execute flow orchestration
        while curr_node:
            # Emit step start
            step_start_event = self.transformer.create_step_start()
            yield step_start_event

            # Set node parameters
            if hasattr(curr_node, 'set_params'):
                curr_node.set_params(params)

            # Create fresh NodeContext for this node
            node_context = NodeContext()

            # Inject context if node supports it
            if isinstance(curr_node, StreamingNodeMixin):
                curr_node.set_context(node_context)

            # Execute node (async or sync)
            if hasattr(curr_node, '_run_async'):
                last_action = await curr_node._run_async(shared)
            else:
                last_action = curr_node._run(shared)

            # Emit events that were collected during node execution
            node_events = node_context.get_events()
            for event in node_events:
                yield event

            # Clean up context
            if isinstance(curr_node, StreamingNodeMixin):
                curr_node.clear_context()

            # Emit step finish
            step_finish_event = self.transformer.create_step_finish()
            yield step_finish_event

            # Get next node
            curr_node = copy.copy(self.flow.get_next_node(curr_node, last_action))

    async def run_stream_sse(self, shared: Dict[str, Any]) -> AsyncIterator[str]:
        """
        Execute the async flow with Server-Sent Events (SSE) formatted output.

        Args:
            shared: Shared state dictionary for the flow

        Yields:
            SSE-formatted strings ready for FastAPI streaming
        """
        async for event in self.run_stream(shared):
            yield format_ai_sdk_sse_event(event)

        # Final DONE event
        yield create_done_event()


# Convenience functions
def wrap_flow_for_streaming(flow: Any) -> StreamingFlow:
    """
    Wrap a PocketFlow Flow to add streaming capabilities.

    Args:
        flow: PocketFlow Flow instance

    Returns:
        StreamingFlow instance
    """
    return StreamingFlow(flow)


def wrap_async_flow_for_streaming(async_flow: Any) -> AsyncStreamingFlow:
    """
    Wrap a PocketFlow AsyncFlow to add streaming capabilities.

    Args:
        async_flow: PocketFlow AsyncFlow instance

    Returns:
        AsyncStreamingFlow instance
    """
    return AsyncStreamingFlow(async_flow)


async def stream_flow_execution(
    flow: Any,
    shared: Dict[str, Any]
) -> AsyncIterator[AiSdkEvent]:
    """
    Convenience function to stream any PocketFlow Flow execution.

    Args:
        flow: PocketFlow Flow or AsyncFlow instance
        shared: Shared state dictionary for the flow

    Yields:
        AiSdkEvent objects in AI-SDK compatible format
    """
    # Auto-detect flow type and wrap appropriately
    wrapper: Union[AsyncStreamingFlow, StreamingFlow]
    if hasattr(flow, '_run_async') or hasattr(flow, 'run_async'):
        # AsyncFlow
        wrapper = AsyncStreamingFlow(flow)
    else:
        # Regular Flow
        wrapper = StreamingFlow(flow)

    async for event in wrapper.run_stream(shared):
        yield event


async def stream_flow_execution_sse(
    flow: Any,
    shared: Dict[str, Any]
) -> AsyncIterator[str]:
    """
    Convenience function to stream any PocketFlow Flow execution as SSE.

    Args:
        flow: PocketFlow Flow or AsyncFlow instance
        shared: Shared state dictionary for the flow

    Yields:
        SSE-formatted strings ready for FastAPI streaming
    """
    async for event in stream_flow_execution(flow, shared):
        yield format_ai_sdk_sse_event(event)

    # Final DONE event
    yield create_done_event()