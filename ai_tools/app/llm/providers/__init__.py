from ai_tools.app.llm.factory import LLMFactory

from .ollama import OllamaClient
from .gemini import GeminiClient

LLMFactory.register("ollama", OllamaClient)
LLMFactory.register("gemini", GeminiClient)
