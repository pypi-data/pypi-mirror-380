"""Pydantic schemas for Agent Manager API I/O."""

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from .domain import AgentFramework, AgentStatus


class AgentCreateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = Field(None, max_length=1000)
    framework: AgentFramework
    config: dict[str, Any] = Field(default_factory=dict)
    environment_variables: dict[str, str] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)


class AgentUpdateRequest(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, max_length=1000)
    config: dict[str, Any] | None = None
    environment_variables: dict[str, str] | None = None
    tags: list[str] | None = None


class AgentRunRequest(BaseModel):
    input_data: dict[str, Any]
    trace_id: str | None = Field(None, max_length=100)


class AgentResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    framework: AgentFramework
    status: AgentStatus
    config: dict[str, Any]
    environment_variables: dict[str, str]
    version: str
    tags: list[str]
    tenant_id: UUID
    created_at: datetime
    updated_at: datetime
    deployed_at: datetime | None
    total_runs: int
    success_rate: float | None
    avg_response_time_ms: float | None

    class Config:
        from_attributes = True


class AgentSummaryResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    framework: AgentFramework
    status: AgentStatus
    version: str
    tags: list[str]
    created_at: datetime
    updated_at: datetime
    total_runs: int
    success_rate: float | None

    class Config:
        from_attributes = True


class AgentRunResponse(BaseModel):
    id: UUID
    agent_id: UUID
    tenant_id: UUID
    input_data: dict[str, Any]
    output_data: dict[str, Any] | None
    status: str
    started_at: datetime
    completed_at: datetime | None
    error_message: str | None
    response_time_ms: float | None
    tokens_used: int | None
    cost_usd: float | None
    trace_id: str | None
    span_id: str | None

    class Config:
        from_attributes = True


class AgentRunSummaryResponse(BaseModel):
    id: UUID
    agent_id: UUID
    status: str
    started_at: datetime
    completed_at: datetime | None
    response_time_ms: float | None
    tokens_used: int | None
    cost_usd: float | None

    class Config:
        from_attributes = True


class PaginatedResponse(BaseModel):
    total: int
    limit: int
    offset: int
    has_more: bool


class PaginatedAgentsResponse(PaginatedResponse):
    items: list[AgentSummaryResponse]


class PaginatedRunsResponse(PaginatedResponse):
    items: list[AgentRunSummaryResponse]


class AgentStatsResponse(BaseModel):
    total_agents: int
    active_agents: int
    total_runs_today: int
    total_runs_this_month: int
    avg_success_rate: float | None
    avg_response_time_ms: float | None


