from pydantic import BaseModel
from typing import Optional


class AIModelConfig(BaseModel):
    provider: str
    model: str
    api_key: Optional[str] = None
