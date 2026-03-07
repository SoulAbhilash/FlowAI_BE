from typing import Type

from annotated_types import T
import httpx

from ai_tools.app.llm.interface import LLMClient
from ai_tools.app.llm.factory import register


@register("ollama")
class OllamaClient(LLMClient):
    def __init__(self, model: str):
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"

    async def generate(self, prompt: str, response_schema: Type[T]) -> T:
        json_schema = response_schema.model_json_schema()

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "format": json_schema,
                },
            )

            response.raise_for_status()

            raw = response.json()["response"]

            return response_schema.model_validate_json(raw)
