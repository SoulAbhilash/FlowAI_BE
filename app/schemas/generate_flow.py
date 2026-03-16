from pydantic import BaseModel

from app.schemas.ai_request import AIRequest


class FlowData(BaseModel):
    flow_name: str
    flow_steps: str


class GenerateFlow(AIRequest[FlowData]):
    pass
