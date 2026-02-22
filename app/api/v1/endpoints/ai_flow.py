from fastapi import APIRouter, Depends, HTTPException, status
import json

from app.schemas.generate_flow import GenerateFlow
from app.core.security import get_current_user
from  ai_tools.app.llm.parser import FlowParser

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/generate_flow")
def generate_flow(generate_flow: GenerateFlow):
    parser = FlowParser()
    json_flow = parser.parse(flow_name=generate_flow.flow_name, text=generate_flow.flow_steps)
    return  json_flow