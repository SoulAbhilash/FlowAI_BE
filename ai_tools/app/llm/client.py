import requests

class OllamaClient:
    def __init__(self, model="llama3:8b"):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt: str) -> str:
        response = requests.post(
            self.base_url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }
        )
        response.raise_for_status()
        return response.json()["response"]
