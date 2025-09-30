import uuid
from datetime import datetime
from enum import Enum
from typing import Any

from a2a.types import DataPart, Message, Part, Role
from pydantic import BaseModel


class ToolStatus(Enum):
    STARTED = "started"
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentTool(BaseModel):
    tool_call_id: str
    tool_name: str
    tool_status: ToolStatus
    tool_args: dict[str, Any]
    tool_result: Any | None = None
    error_message: str | None = None
    execution_time_ms: float | None = None
    created_at: datetime | None = None


class ReasoningStep(BaseModel):
    title: str | None = None
    action: str | None = None
    result: str | None = None
    reasoning: str | None = None
    next_action: str | None = None
    confidence: float | None = None


def new_agent_reasoning_message(
    reasoning_content: str | list[ReasoningStep],
    context_id: str | None = None,
    task_id: str | None = None,
) -> Message:
    """
    Creates a new agent message containing reasoning content.

    Args:
        reasoning_content: Either a string of reasoning text or a list of ReasoningStep objects.
        context_id: The context ID for the message.
        task_id: The task ID for the message.

    Returns:
        A new `Message` object with role 'agent' containing the reasoning content.
    """
    if isinstance(reasoning_content, str):
        # Simple text reasoning
        return Message(
            role=Role.agent,
            parts=[
                Part(
                    root=DataPart(
                        data={"text": reasoning_content}, metadata={"type": "reasoning"}
                    )
                )
            ],
            message_id=str(uuid.uuid4()),
            task_id=task_id,
            context_id=context_id,
        )
    else:
        # Structured reasoning steps
        steps_data = [step.model_dump() for step in reasoning_content]
        return Message(
            role=Role.agent,
            parts=[
                Part(
                    root=DataPart(
                        data={"steps": steps_data}, metadata={"type": "reasoning"}
                    )
                )
            ],
            message_id=str(uuid.uuid4()),
            task_id=task_id,
            context_id=context_id,
        )


def new_agent_tools_message(
    tools: list[AgentTool],
    context_id: str | None = None,
    task_id: str | None = None,
) -> Message:
    """
    Creates a new agent message containing tools information.

    Args:
        tools: A list of AgentTool objects.
        context_id: The context ID for the message.
        task_id: The task ID for the message.

    Returns:
        A new `Message` object with role 'agent' containing the tools data.
    """
    return Message(
        role=Role.agent,
        parts=[
            Part(
                root=DataPart(
                    data={"tools": [tool.model_dump(mode="json") for tool in tools]},
                    metadata={"type": "tools"},
                )
            )
        ],
        message_id=str(uuid.uuid4()),
        task_id=task_id,
        context_id=context_id,
    )


def create_reasoning_step(
    title: str | None = None,
    action: str | None = None,
    result: str | None = None,
    reasoning: str | None = None,
    next_action: str | None = None,
    confidence: float | None = None,
) -> ReasoningStep:
    """
    Helper function to create a ReasoningStep.

    Args:
        title: Title of the reasoning step.
        action: Action taken in this step.
        result: Result of the action.
        reasoning: Explanation or reasoning behind the action.
        next_action: Suggested next action.
        confidence: Confidence level in the action/result.

    Returns:
        A new ReasoningStep object.
    """
    return ReasoningStep(
        title=title,
        action=action,
        result=result,
        reasoning=reasoning,
        next_action=next_action,
        confidence=confidence,
    )


def create_agent_tool(
    tool_call_id: str,
    tool_name: str,
    tool_args: dict[str, Any],
    tool_status: ToolStatus = ToolStatus.PENDING,
    tool_result: Any | None = None,
    error_message: str | None = None,
    execution_time_ms: float | None = None,
    created_at: datetime | None = None,
) -> AgentTool:
    """
    Helper function to create an AgentTool.

    Args:
        tool_call_id: Unique identifier for the tool call.
        tool_name: Name of the tool.
        tool_args: Arguments passed to the tool.
        tool_status: Current status of the tool (default is PENDING).
        tool_result: Result returned by the tool, if any.
        error_message: Error message if the tool failed, if any.
        execution_time_ms: Execution time in milliseconds, if available.
        created_at: Timestamp when the tool was created, if available.

    Returns:
        A new AgentTool object.
    """
    return AgentTool(
        tool_call_id=tool_call_id,
        tool_name=tool_name,
        tool_status=tool_status,
        tool_args=tool_args,
        tool_result=tool_result,
        error_message=error_message,
        execution_time_ms=execution_time_ms,
        created_at=created_at,
    )
