"""Top-level engine configuration models."""

from typing import Literal, Any

from pydantic import BaseModel, Field

from idun_agent_schema.engine.haystack import HaystackAgentConfig

from .agent import BaseAgentConfig
from .langgraph import LangGraphAgentConfig
from .server import ServerConfig


class AgentConfig(BaseModel):
    """Configuration for agent specification and settings."""

    type: Literal["langgraph", "ADK", "CREWAI", "haystack"] = Field(default="langgraph")
    config: Any = Field(description="Specific agent config")


config: BaseAgentConfig | HaystackAgentConfig | LangGraphAgentConfig = Field(
    default_factory=BaseAgentConfig
)


class EngineConfig(BaseModel):
    """Main engine configuration model for the entire Idun Agent Engine."""

    server: ServerConfig = Field(default_factory=ServerConfig)
    agent: AgentConfig
