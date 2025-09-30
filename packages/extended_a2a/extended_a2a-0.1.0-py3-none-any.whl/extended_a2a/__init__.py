"""
Extended A2A (Agent-to-Agent) Communication Library

This package extends the base a2a-sdk with rich message types for advanced agent communication,
including reasoning chains, tool executions.
"""

from .auth_plugin import (
    # Authentication
    AuthCallContextBuilder,
    AuthenticatedRequestHandler,
)
from .types import (
    # Models
    AgentTool,
    ReasoningStep,
    # Enums
    ToolStatus,
    # Helper functions
    create_agent_tool,
    create_reasoning_step,
    # Message creators
    new_agent_reasoning_message,
    new_agent_tools_message,
)

__version__ = "0.1.0"
__author__ = "hienhayho"
__email__ = "hienhayho3002@gmail.com"

__all__ = [
    # Enums
    "ToolStatus",
    "ReasoningType",
    # Models
    "AgentTool",
    # Message creators
    "new_agent_reasoning_message",
    "new_agent_tools_message",
    # Helper functions
    "create_reasoning_step",
    "create_agent_tool",
    # Authentication
    "AuthCallContextBuilder",
    "AuthenticatedRequestHandler",
]
