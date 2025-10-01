"""
AI-SDK compatible event transformation for AgentFlow streaming.

This module converts internal StreamEvent objects to AI-SDK compatible format
for frontend integration with AI libraries and frameworks.
"""

from typing import Dict, Any, List, Iterator, Union
from dataclasses import dataclass
from enum import Enum
import json
import uuid

from ..llm_agno import (
    StreamEvent,
    StreamEventType,
    ToolCallStartedEvent,
    ToolCallCompletedEvent,
    AssistantResponseEvent,
    ModelResponseCompleteEvent,
)


class AiSdkEventType(str, Enum):
    """AI-SDK compatible event types"""

    START = "start"
    START_STEP = "start-step"
    FINISH_STEP = "finish-step"
    FINISH = "finish"
    TOOL_INPUT_START = "tool-input-start"
    TOOL_INPUT_DELTA = "tool-input-delta"
    TOOL_INPUT_AVAILABLE = "tool-input-available"
    TOOL_OUTPUT_AVAILABLE = "tool-output-available"
    TEXT_START = "text-start"
    TEXT_DELTA = "text-delta"
    TEXT_END = "text-end"
    ERROR = "error"


@dataclass
class AiSdkEvent:
    """Base class for AI-SDK compatible events"""

    type: Union[AiSdkEventType, str]
    data: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format for JSON serialization"""
        if isinstance(self.type, AiSdkEventType):
            type_value = self.type.value
        else:
            type_value = self.type
        result = {"type": type_value}
        result.update(self.data)
        return result

    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), separators=(",", ":"))


# Flow-level events
class FlowStartEvent(AiSdkEvent):
    def __init__(self, message_id: str = None):
        if message_id is None:
            message_id = f"msg_{str(uuid.uuid4())}"
        super().__init__(AiSdkEventType.START, {"messageId": message_id})


class FlowFinishEvent(AiSdkEvent):
    def __init__(self):
        super().__init__(AiSdkEventType.FINISH, {})


class StepStartEvent(AiSdkEvent):
    def __init__(self, step_name: str = None, step_type: str = None):
        data = {}
        if step_name:
            data["stepName"] = step_name
        if step_type:
            data["stepType"] = step_type
        super().__init__(AiSdkEventType.START_STEP, data)


class StepFinishEvent(AiSdkEvent):
    def __init__(self, step_name: str = None, step_type: str = None):
        data = {}
        if step_name:
            data["stepName"] = step_name
        if step_type:
            data["stepType"] = step_type
        super().__init__(AiSdkEventType.FINISH_STEP, data)


# Tool call events
class ToolInputStartEvent(AiSdkEvent):
    def __init__(self, tool_call_id: str, tool_name: str):
        super().__init__(
            AiSdkEventType.TOOL_INPUT_START,
            {"toolCallId": tool_call_id, "toolName": tool_name},
        )


class ToolInputDeltaEvent(AiSdkEvent):
    def __init__(self, tool_call_id: str, input_text_delta: str):
        super().__init__(
            AiSdkEventType.TOOL_INPUT_DELTA,
            {"toolCallId": tool_call_id, "inputTextDelta": input_text_delta},
        )


class ToolInputAvailableEvent(AiSdkEvent):
    def __init__(self, tool_call_id: str, tool_name: str, input_data: Dict[str, Any]):
        super().__init__(
            AiSdkEventType.TOOL_INPUT_AVAILABLE,
            {"toolCallId": tool_call_id, "toolName": tool_name, "input": input_data},
        )


class ToolOutputAvailableEvent(AiSdkEvent):
    def __init__(
        self, tool_call_id: str, output: Dict[str, Any], preliminary: bool = False
    ):
        super().__init__(
            AiSdkEventType.TOOL_OUTPUT_AVAILABLE,
            {"toolCallId": tool_call_id, "output": output, "preliminary": preliminary},
        )


# Text streaming events
class TextStartEvent(AiSdkEvent):
    def __init__(self, text_id: str = None):
        if text_id is None:
            text_id = f"txt-{str(uuid.uuid4())[:8]}"
        super().__init__(AiSdkEventType.TEXT_START, {"id": text_id})


class TextDeltaEvent(AiSdkEvent):
    def __init__(self, text_id: str, delta: str):
        super().__init__(AiSdkEventType.TEXT_DELTA, {"id": text_id, "delta": delta})


class TextEndEvent(AiSdkEvent):
    def __init__(self, text_id: str):
        super().__init__(AiSdkEventType.TEXT_END, {"id": text_id})


class StreamEventTransformer:
    """Transforms internal StreamEvent objects to AI-SDK compatible events"""

    def __init__(self):
        self.active_text_streams: Dict[str, str] = {}  # Maps context to text_id
        self.tool_call_states: Dict[
            str, Dict[str, Any]
        ] = {}  # Track tool call progression

    def transform_event(self, event: StreamEvent) -> List[AiSdkEvent]:
        """
        Transform a single StreamEvent to one or more AI-SDK events.

        Args:
            event: StreamEvent to transform

        Returns:
            List of AiSdkEvent objects
        """
        if isinstance(event, ToolCallStartedEvent):
            return self._transform_tool_call_started(event)
        elif isinstance(event, ToolCallCompletedEvent):
            return self._transform_tool_call_completed(event)
        elif isinstance(event, AssistantResponseEvent):
            return self._transform_assistant_response(event)
        elif isinstance(event, ModelResponseCompleteEvent):
            return self._transform_model_response_complete(event)
        else:
            # Unknown event type, skip
            return []

    def _transform_tool_call_started(
        self, event: ToolCallStartedEvent
    ) -> List[AiSdkEvent]:
        """Transform ToolCallStartedEvent to AI-SDK tool events"""
        events = []

        # Tool input start
        events.append(
            ToolInputStartEvent(
                tool_call_id=event.tool_call_id, tool_name=event.tool_name
            )
        )

        # Convert args to JSON string for delta streaming
        args_json = json.dumps(event.tool_args, separators=(",", ":"))

        # Generate delta events for arguments (if available from streaming)
        if args_json and args_json != "{}":
            # For now, emit the complete args as one delta
            events.append(
                ToolInputDeltaEvent(
                    tool_call_id=event.tool_call_id, input_text_delta=args_json
                )
            )

        # Tool input available (complete args)
        events.append(
            ToolInputAvailableEvent(
                tool_call_id=event.tool_call_id,
                tool_name=event.tool_name,
                input_data=event.tool_args,
            )
        )

        # Store tool call state for completion
        self.tool_call_states[event.tool_call_id] = {
            "tool_name": event.tool_name,
            "input": event.tool_args,
        }

        return events

    def _transform_tool_call_completed(
        self, event: ToolCallCompletedEvent
    ) -> List[AiSdkEvent]:
        """Transform ToolCallCompletedEvent to AI-SDK tool output event"""
        # For now, we'll create a simple success output
        # In a real implementation, this would come from actual tool execution
        output = {
            "status": "success",
            "result": event.tool_args,  # This would be the actual tool result
            "text": f"Tool {event.tool_name} executed successfully",
        }

        return [
            ToolOutputAvailableEvent(
                tool_call_id=event.tool_call_id, output=output, preliminary=False
            )
        ]

    def _transform_assistant_response(
        self, event: AssistantResponseEvent
    ) -> List[AiSdkEvent]:
        """Transform AssistantResponseEvent to AI-SDK text events"""
        events = []

        # Use a default text stream ID if none exists
        text_id = self.active_text_streams.get("default")
        if text_id is None:
            text_id = f"txt-{str(uuid.uuid4())[:8]}"
            self.active_text_streams["default"] = text_id
            events.append(TextStartEvent(text_id=text_id))

        # Text delta
        events.append(TextDeltaEvent(text_id=text_id, delta=event.content))

        return events

    def _transform_model_response_complete(
        self, event: ModelResponseCompleteEvent
    ) -> List[AiSdkEvent]:
        """Transform ModelResponseCompleteEvent to text end event"""
        events = []

        # End any active text streams
        for text_id in self.active_text_streams.values():
            events.append(TextEndEvent(text_id=text_id))

        # Clear active streams
        self.active_text_streams.clear()

        return events

    def create_flow_start(self) -> AiSdkEvent:
        """Create flow start event"""
        return FlowStartEvent()

    def create_flow_finish(self) -> AiSdkEvent:
        """Create flow finish event"""
        return FlowFinishEvent()

    def create_step_start(
        self, step_name: str = None, step_type: str = None
    ) -> AiSdkEvent:
        """Create step start event"""
        return StepStartEvent(step_name=step_name, step_type=step_type)

    def create_step_finish(
        self, step_name: str = None, step_type: str = None
    ) -> AiSdkEvent:
        """Create step finish event"""
        return StepFinishEvent(step_name=step_name, step_type=step_type)


def transform_stream_events(events: Iterator[StreamEvent]) -> Iterator[AiSdkEvent]:
    """
    Transform a stream of internal StreamEvent objects to AI-SDK compatible events.

    Args:
        events: Iterator of StreamEvent objects

    Yields:
        AiSdkEvent objects in AI-SDK compatible format
    """
    transformer = StreamEventTransformer()

    # Flow start
    yield transformer.create_flow_start()

    # Transform each event
    for event in events:
        ai_sdk_events = transformer.transform_event(event)
        for ai_sdk_event in ai_sdk_events:
            yield ai_sdk_event

    # Flow finish
    yield transformer.create_flow_finish()


def format_ai_sdk_sse_event(event: AiSdkEvent) -> str:
    """
    Format an AI-SDK event as Server-Sent Event (SSE) for FastAPI streaming.

    Args:
        event: AiSdkEvent to format

    Returns:
        SSE-formatted string with data: prefix and double newlines
    """
    return f"data: {event.to_json()}\n\n"


def create_done_event() -> str:
    """Create the final [DONE] event for AI-SDK streaming"""
    return "data: [DONE]\n\n"
