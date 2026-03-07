import requests
import httpx

class OllamaClient:
    def __init__(self, model: str):
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"
        self.timeout = httpx.Timeout(120.0)

    async def generate(self, prompt: str) -> str:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
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
        
class GeminiClient:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    async def generate(self, prompt: str) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{url}?key={self.api_key}",
                json={
                    "contents": [
                        {"parts": [{"text": prompt}]}
                    ]
                },
            )
            response.raise_for_status()
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]

