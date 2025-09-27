__author__ = "captainSuo"
__version__ = "0.2.0"
__all__ = [
    "Agent",
    "Agent",
    "AsyncFunctionTool",
    "Tool",
    "FoldableAsyncFunctionTool",
    "FoldableFunctionTool",
    "FoldableMCPTool",
    "FunctionTool",
    "MCPClient",
    "MCPTool",
    "GUIAgent",
]


from .agent.agent_async import Agent
from .agent.function_tool import (
    FunctionTool,
    FoldableFunctionTool,
    AsyncFunctionTool,
    FoldableAsyncFunctionTool,
)
from .agent.mcp_tool import MCPClient, MCPTool, FoldableMCPTool
from .agent.base_tool import Tool

try:
    from .gui_agent import GUIAgent
except ImportError:
    pass  # GUIAgent is optional
