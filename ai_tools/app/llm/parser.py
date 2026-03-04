import json
from ai_tools.app.llm.interface import LLMClient
from ai_tools.app.llm.prompts import GENERATE_GRAPH_PROMPT

class FlowParser:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    async def parse(self, text: str, flow_name: str) -> dict:
        prompt = f"""
{GENERATE_GRAPH_PROMPT}

Flow name: {flow_name}
User description:
{text}
"""

        raw_string = await self.llm.generate(prompt)

        try:
            return json.loads(raw_string)
        except json.JSONDecodeError:
            return {
                "error": "Invalid JSON returned from LLM",
                "content": raw_string,
            }