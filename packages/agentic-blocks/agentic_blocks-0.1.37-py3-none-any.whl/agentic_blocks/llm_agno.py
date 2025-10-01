from typing import List, Dict, Any, Optional, Union, Iterator
from dataclasses import dataclass
from enum import Enum

from agno.models.openrouter import OpenRouter
from agno.models.message import Message
from agno.models.response import ModelResponse

from agentic_blocks.utils.config_utils import get_llm_config
from agentic_blocks.utils.tools_utils import agno_tools_to_openai_format
from agentic_blocks.messages import Messages


__all__ = [
    "invoke_stream",
    "call_llm_stream",
    "parse_model_response_stream",
    "convert_tools",
    "StreamEventType",
    "StreamEvent",
    "ToolCallStartedEvent",
    "ToolCallCompletedEvent",
    "AssistantResponseEvent",
    "ModelResponseCompleteEvent",
    "StreamResponse",
]


class StreamEventType(str, Enum):
    """Events that can be emitted during LLM streaming"""

    tool_call_started = "tool_call_started"
    tool_call_completed = "tool_call_completed"
    assistant_response = "assistant_response"
    model_response_complete = "model_response_complete"


@dataclass
class StreamEvent:
    """Base class for streaming events"""

    event_type: StreamEventType


@dataclass
class ToolCallStartedEvent(StreamEvent):
    """Event emitted when a tool call begins"""

    tool_call_id: str
    tool_name: str
    tool_args: Dict[str, Any]

    def __init__(self, tool_call_id: str, tool_name: str, tool_args: Dict[str, Any]):
        self.event_type = StreamEventType.tool_call_started
        self.tool_call_id = tool_call_id
        self.tool_name = tool_name
        self.tool_args = tool_args


@dataclass
class ToolCallCompletedEvent(StreamEvent):
    """Event emitted when a tool call completes"""

    tool_call_id: str
    tool_name: str
    tool_args: Dict[str, Any]

    def __init__(self, tool_call_id: str, tool_name: str, tool_args: Dict[str, Any]):
        self.event_type = StreamEventType.tool_call_completed
        self.tool_call_id = tool_call_id
        self.tool_name = tool_name
        self.tool_args = tool_args


@dataclass
class AssistantResponseEvent(StreamEvent):
    """Event emitted for assistant text content"""

    content: str

    def __init__(self, content: str):
        self.event_type = StreamEventType.assistant_response
        self.content = content


@dataclass
class ModelResponseCompleteEvent(StreamEvent):
    """Event emitted when model response is complete"""

    final_response: ModelResponse

    def __init__(self, final_response: ModelResponse):
        self.event_type = StreamEventType.model_response_complete
        self.final_response = final_response


class StreamResponse:
    """Response object with immediate return and on-demand tool call determination"""

    def __init__(
        self,
        event_stream: Iterator[
            Union[
                AssistantResponseEvent,
                ToolCallStartedEvent,
                ToolCallCompletedEvent,
                ModelResponseCompleteEvent,
            ]
        ],
    ):
        self._original_stream = event_stream
        self._cached_tool_calls: Union[List[Dict[str, Any]], None] = None
        self._all_cached_events: List[
            Union[
                AssistantResponseEvent,
                ToolCallStartedEvent,
                ToolCallCompletedEvent,
                ModelResponseCompleteEvent,
            ]
        ] = []
        self._stream_fully_consumed = False
        self._tool_calls_processed = False
        self.content = ""

    def _ensure_all_events_cached(self):
        """Consume remaining stream and cache all events if not already done"""
        if self._stream_fully_consumed:
            return

        # Consume all remaining events from original stream
        for event in self._original_stream:
            self._all_cached_events.append(event)

        self._stream_fully_consumed = True

    def tool_calls(self) -> List[Dict[str, Any]]:
        """
        Blocking function that determines tool calls by reading stream until decision can be made.

        Returns:
            List of tool calls, or empty list if no tools detected
        """
        if self._cached_tool_calls is not None:
            return self._cached_tool_calls

        # If stream already consumed (e.g., via event_stream access), process cached events
        if self._stream_fully_consumed or self._all_cached_events:
            return self._process_cached_events_for_tool_calls()

        # Block here and read stream until we can determine tool calls
        self._cached_tool_calls = []

        for event in self._original_stream:
            self._all_cached_events.append(event)

            # Early detection: Tool calls found!
            if isinstance(event, ToolCallStartedEvent):
                partial_tool_call = {
                    "id": event.tool_call_id,
                    "type": "function",
                    "function": {"name": event.tool_name, "arguments": "{}"},
                }
                self._cached_tool_calls.append(partial_tool_call)

                # Continue reading to get complete tool calls
                self._read_remaining_tool_calls()
                break

            # Early abort: Content detected, no tools coming
            elif isinstance(event, AssistantResponseEvent):
                self._cached_tool_calls = []  # No tools
                self.content += event.content
                # No need to consume entire stream - we know there are no tools
                break

        self._tool_calls_processed = True
        return self._cached_tool_calls

    def _process_cached_events_for_tool_calls(self) -> List[Dict[str, Any]]:
        """Process cached events to extract tool calls when stream was already consumed"""
        import json

        self._cached_tool_calls = []
        tool_calls_map = {}  # Map tool_call_id to tool call dict

        for event in self._all_cached_events:
            if isinstance(event, ToolCallStartedEvent):
                tool_call = {
                    "id": event.tool_call_id,
                    "type": "function",
                    "function": {"name": event.tool_name, "arguments": "{}"},
                }
                self._cached_tool_calls.append(tool_call)
                tool_calls_map[event.tool_call_id] = tool_call

            elif isinstance(event, ToolCallCompletedEvent):
                # Update the arguments with completed values
                if event.tool_call_id in tool_calls_map:
                    tool_calls_map[event.tool_call_id]["function"]["arguments"] = (
                        json.dumps(event.tool_args)
                        if isinstance(event.tool_args, dict)
                        else event.tool_args
                    )

            elif isinstance(event, AssistantResponseEvent):
                # If we see content, there are no tool calls
                self._cached_tool_calls = []
                self.content += event.content
                break

        return self._cached_tool_calls

    def _read_remaining_tool_calls(self):
        """Continue reading stream to get complete tool calls after first detection"""
        for event in self._original_stream:
            self._all_cached_events.append(event)

            if isinstance(event, ToolCallStartedEvent):
                # Additional tool call
                partial_tool_call = {
                    "id": event.tool_call_id,
                    "type": "function",
                    "function": {"name": event.tool_name, "arguments": "{}"},
                }
                self._cached_tool_calls.append(partial_tool_call)

            elif isinstance(event, ToolCallCompletedEvent):
                # Update existing tool call with complete arguments
                import json

                for tc in self._cached_tool_calls:
                    if tc["id"] == event.tool_call_id:
                        tc["function"]["arguments"] = (
                            json.dumps(event.tool_args)
                            if isinstance(event.tool_args, dict)
                            else event.tool_args
                        )

            elif isinstance(event, ModelResponseCompleteEvent):
                # Stream complete, finalize content
                self.content = event.final_response.content or self.content
                break

        # Mark stream as fully consumed
        self._stream_fully_consumed = True

    def _create_hybrid_iterator(self):
        """Return cached events + remaining stream events"""
        # First yield all cached events
        for event in self._all_cached_events:
            yield event

        # Then yield remaining events from stream (if any)
        for event in self._original_stream:
            self._all_cached_events.append(event)
            yield event

        self._stream_fully_consumed = True

    def _create_caching_iterator(self):
        """Return streaming iterator that caches events as they're consumed"""
        for event in self._original_stream:
            self._all_cached_events.append(event)
            yield event

        self._stream_fully_consumed = True

    @property
    def event_stream(
        self,
    ) -> Iterator[
        Union[
            AssistantResponseEvent,
            ToolCallStartedEvent,
            ToolCallCompletedEvent,
            ModelResponseCompleteEvent,
        ]
    ]:
        """Returns an iterator over all events. First access streams live, subsequent access returns cached events."""
        # If stream already fully consumed, return cached events
        if self._stream_fully_consumed:
            return iter(self._all_cached_events)

        # If we've partially consumed via tool_calls(), return hybrid iterator
        if self._all_cached_events:
            return self._create_hybrid_iterator()

        # First access - return true streaming iterator that caches as it goes
        return self._create_caching_iterator()

    def print_content_stream(self):
        """
        Print assistant response content as a stream of words.

        This method consumes the event stream and prints only the content from
        AssistantResponseEvent events, creating a live streaming text effect.
        """
        import sys

        for event in self.event_stream:
            if isinstance(event, AssistantResponseEvent):
                print(event.content, end="", flush=True)

        # Print a newline at the end for clean formatting
        print()


def parse_model_response_stream(
    model_responses: Iterator[ModelResponse],
) -> Iterator[
    Union[
        AssistantResponseEvent,
        ToolCallStartedEvent,
        ToolCallCompletedEvent,
        ModelResponseCompleteEvent,
    ]
]:
    """
    Convert a stream of ModelResponse objects into granular events for tool calls and content.

    Args:
        model_responses: Iterator of ModelResponse objects (e.g., from invoke())

    Returns:
        Iterator of StreamEvent objects for fine-grained streaming control
    """
    import json

    # Track tool calls by ID to detect start/completion
    tracked_tool_calls: Dict[str, Dict[str, Any]] = {}
    final_response = None
    accumulated_content = ""

    for model_response in model_responses:
        final_response = model_response

        # Yield assistant content events and accumulate content
        if model_response.content:
            accumulated_content += model_response.content
            yield AssistantResponseEvent(content=model_response.content)

        # Process tool calls
        if hasattr(model_response, "tool_calls") and model_response.tool_calls:
            current_tool_calls = model_response.tool_calls

            # Check for new or updated tool calls
            for tool_call in current_tool_calls:
                # Handle both new ChoiceDeltaToolCall format and old dict format
                if hasattr(tool_call, 'id'):
                    # New ChoiceDeltaToolCall format
                    tool_call_id = tool_call.id or ""
                    tool_name = tool_call.function.name if tool_call.function else ""
                    arguments_raw = tool_call.function.arguments if tool_call.function else ""
                else:
                    # Old dict format (backward compatibility)
                    tool_call_id = tool_call.get("id", "")
                    function_info = tool_call.get("function", {})
                    tool_name = function_info.get("name", "")
                    arguments_raw = function_info.get("arguments", "")

                # Handle empty tool call IDs by finding the most recent incomplete tool call
                if not tool_call_id:
                    # Find the most recent incomplete tool call to associate this chunk with
                    for tracked_id, tracked_info in tracked_tool_calls.items():
                        if not tracked_info["completed"]:
                            tool_call_id = tracked_id
                            tool_name = tracked_info["name"]
                            break

                    # If no incomplete tool call found, skip this chunk
                    if not tool_call_id:
                        continue

                # Track new tool calls
                if tool_call_id not in tracked_tool_calls:
                    # Initialize accumulated arguments
                    accumulated_arguments = arguments_raw if isinstance(arguments_raw, str) else ""

                    # Parse initial arguments if available
                    initial_args = {}
                    arguments_complete = False
                    if accumulated_arguments.strip():
                        try:
                            initial_args = json.loads(accumulated_arguments)
                            arguments_complete = True
                        except (json.JSONDecodeError, TypeError):
                            pass

                    tracked_tool_calls[tool_call_id] = {
                        "name": tool_name,
                        "accumulated_arguments": accumulated_arguments,
                        "last_args_length": len(accumulated_arguments),
                        "completed": arguments_complete,
                    }

                    # Only emit started event if we have the tool name
                    if tool_name:
                        yield ToolCallStartedEvent(
                            tool_call_id=tool_call_id,
                            tool_name=tool_name,
                            tool_args=initial_args,
                        )

                        # If arguments are complete immediately, emit completion event too
                        if arguments_complete:
                            yield ToolCallCompletedEvent(
                                tool_call_id=tool_call_id,
                                tool_name=tool_name,
                                tool_args=initial_args,
                            )

                # Check if tool call is complete
                elif not tracked_tool_calls[tool_call_id]["completed"]:
                    # Accumulate new arguments to existing ones
                    current_accumulated = tracked_tool_calls[tool_call_id]["accumulated_arguments"]
                    new_arguments = arguments_raw if isinstance(arguments_raw, str) else ""

                    # Append new arguments to accumulated arguments
                    updated_accumulated = current_accumulated + new_arguments
                    tracked_tool_calls[tool_call_id]["accumulated_arguments"] = updated_accumulated

                    current_args_length = len(updated_accumulated)

                    # Tool call is complete when arguments stop growing and we have valid JSON
                    arguments_complete = False
                    parsed_args = {}

                    if updated_accumulated.strip():
                        try:
                            parsed_args = json.loads(updated_accumulated)
                            arguments_complete = True
                        except (json.JSONDecodeError, TypeError):
                            # Arguments still streaming, not complete
                            pass

                    # Update length tracking
                    tracked_tool_calls[tool_call_id]["last_args_length"] = current_args_length

                    # Emit completion event if arguments are complete
                    # For streaming responses, complete when JSON becomes valid
                    if arguments_complete and current_args_length > 0:
                        tracked_tool_calls[tool_call_id]["completed"] = True

                        yield ToolCallCompletedEvent(
                            tool_call_id=tool_call_id,
                            tool_name=tool_name,
                            tool_args=parsed_args,
                        )

    # Yield final complete event if we had any responses
    if final_response is not None:
        # Create a copy of the final response with accumulated content
        final_response_with_content = final_response
        if accumulated_content:
            # Update the content with accumulated content
            final_response_with_content.content = accumulated_content
        yield ModelResponseCompleteEvent(final_response=final_response_with_content)


def invoke_stream(
    messages: Union[List[Message]],
    tools: Optional[List[Any]] = None,
    model: Optional[str] = None,
    **kwargs,
) -> Iterator[ModelResponse]:
    """
    Call LLM with streaming and return ModelResponse events with assembled tool calls.

    Args:
        messages: Either a list of Message instances or a list of message dicts
        tools: Optional list of tools (agno @tool functions or OpenAI format dicts)
        model: Model name to use for completion
        **kwargs: Additional parameters to pass to OpenRouter

    Returns:
        Iterator of ModelResponse objects with assembled tool calls and content
    """
    # Get configuration for model name
    config = get_llm_config(model=model)

    # Initialize OpenRouter client
    model_id = config["model"]
    if not model_id:
        raise ValueError(
            "Model ID is required but not found in configuration or environment variables"
        )
    client = OpenRouter(id=model_id)

    # Convert tools if needed
    converted_tools = convert_tools(tools) if tools else None

    assistant_message = Message(role=client.assistant_message_role)

    return client.invoke_stream(
        messages, assistant_message, tools=converted_tools, **kwargs
    )


def call_llm_stream(
    messages: Union[List[Message], Messages],
    tools: Optional[List[Any]] = None,
    model: Optional[str] = None,
    **kwargs,
) -> StreamResponse:
    """
    Call LLM and return StreamResponse immediately with on-demand tool call determination.

    Args:
        messages: Either a Messages object, a list of Message instances, or a list of message dicts
        tools: Optional list of tools (agno @tool functions or OpenAI format dicts)
        model: Model name to use for completion
        **kwargs: Additional parameters to pass to OpenRouter

    Returns:
        StreamResponse object that returns immediately. Use tool_calls() method for routing decisions.
    """
    # Handle Messages object
    if isinstance(messages, Messages):
        messages = messages.get_messages()

    # Get the base stream from invoke
    model_stream = invoke_stream(messages=messages, tools=tools, model=model, **kwargs)

    # Convert to event stream
    events = parse_model_response_stream(model_stream)

    # Return StreamResponse immediately - no blocking here!
    return StreamResponse(event_stream=events)


def convert_tools(tools: List[Any]) -> List[Dict[str, Any]]:
    """
    Convert agno @tool decorated functions to OpenAI function calling format.
    If tools are already in OpenAI format, returns them unchanged.

    Args:
        tools: List of agno @tool decorated functions or OpenAI format dicts

    Returns:
        List of tools in OpenAI function calling format
    """
    if not tools:
        return []

    # Check if tools are already in OpenAI format
    if isinstance(tools[0], dict) and "type" in tools[0] and "function" in tools[0]:
        return tools

    # Convert agno tools to OpenAI format
    return agno_tools_to_openai_format(tools)
