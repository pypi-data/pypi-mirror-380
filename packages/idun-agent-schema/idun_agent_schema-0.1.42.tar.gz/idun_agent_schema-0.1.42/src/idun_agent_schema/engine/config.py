"""Top-level engine configuration models."""

from typing import Literal

from pydantic import BaseModel, Field

from idun_agent_schema.engine.haystack import HaystackAgentConfig

from .agent import BaseAgentConfig
from .langgraph import LangGraphAgentConfig
from .server import ServerConfig


class AgentConfig(BaseModel):
    """Configuration for agent specification and settings."""

    type: Literal["langgraph", "ADK", "CREWAI", "haystack"] = Field(default="langgraph")
    config: BaseAgentConfig | HaystackAgentConfig | LangGraphAgentConfig


class EngineConfig(BaseModel):
    """Main engine configuration model for the entire Idun Agent Engine."""

    server: ServerConfig = Field(default_factory=ServerConfig)
    agent: AgentConfig
