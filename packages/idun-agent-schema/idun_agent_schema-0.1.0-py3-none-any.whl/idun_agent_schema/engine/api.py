"""Schemas for engine HTTP API request/response payloads."""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    query: str


class ChatResponse(BaseModel):
    session_id: str
    response: str


