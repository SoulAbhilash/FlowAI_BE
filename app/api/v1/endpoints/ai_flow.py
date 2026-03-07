from fastapi import APIRouter, Depends
from app.schemas.generate_flow import GenerateFlow
from ai_tools.app.llm.factory import LLMFactory
from ai_tools.app.llm.parser import FlowParser
from app.core.security import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.post("/generate_flow")
async def generate_flow(request: GenerateFlow):

    llm = LLMFactory.create(
        provider=request.provider,
        model=request.model,
        api_key=request.api_key,
    )

    parser = FlowParser(llm=llm)

    json_flow = await parser.parse(
        flow_name=request.flow_name,
        text=request.flow_steps,
    )

    return json_flow
