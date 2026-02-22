# Pydantic models for request/response data
from pydantic import BaseModel

class GenerateFlow(BaseModel):
    flow_name: str
    flow_steps: str