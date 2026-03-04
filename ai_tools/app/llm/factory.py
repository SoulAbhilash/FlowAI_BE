from client import OllamaClient, GeminiClient
from interface import LLMClient

class LLMFactory:

    @staticmethod
    def create(provider: str, model: str, api_key: str | None) -> LLMClient:
        if provider == "ollama":
            return OllamaClient(model=model)

        elif provider == "gemini":
            if not api_key:
                raise ValueError("Gemini requires api_key")
            return GeminiClient(api_key=api_key, model=model)

        else:
            raise ValueError("Unsupported provider")