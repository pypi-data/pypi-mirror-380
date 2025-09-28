"""FastAPI AgentRouter - AI Agent interface library for FastAPI."""

__version__ = "0.6.4"

from .agents.vertexai import get_vertex_ai_agent_engine
from .core.dependencies import AgentProtocol, get_agent
from .core.routers import router
from .core.settings import Settings, get_settings

__all__ = [
    "AgentProtocol",
    "Settings",
    "__version__",
    "get_agent",
    "get_settings",
    "get_vertex_ai_agent_engine",
    "router",
]
