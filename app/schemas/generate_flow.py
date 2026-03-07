# Pydantic models for request/response data
from pydantic import BaseModel
from typing import Literal

class GenerateFlow(BaseModel):
    provider: Literal["ollama", "gemini"]
    model: str
    api_key: str | None = None
    flow_name: str
    flow_steps: str