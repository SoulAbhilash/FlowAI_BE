import json
import re
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

        # Extract JSON block
        json_match = re.search(r"\{.*\}", raw_string, re.DOTALL)

        if not json_match:
            return {
                "error": "No JSON found in LLM response",
                "content": raw_string,
            }

        json_string = json_match.group(0)

        try:
            return json.loads(json_string)
        except json.JSONDecodeError:
            return {
                "error": "Invalid JSON returned from LLM",
                "content": raw_string,
            }