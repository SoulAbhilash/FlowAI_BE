from typing import Generic, TypeVar

from pydantic import BaseModel

from app.schemas.ai_config import AIModelConfig

T = TypeVar("T")


class AIRequest(BaseModel, Generic[T]):
    config: AIModelConfig
    prompt: T
