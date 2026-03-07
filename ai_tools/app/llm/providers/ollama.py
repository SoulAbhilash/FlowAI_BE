import httpx

from ai_tools.app.llm.interface import LLMClient


class OllamaClient(LLMClient):
    def __init__(self, model: str):
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"

    async def generate(self, prompt: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
            )
            response.raise_for_status()
            return response.json()["response"]
