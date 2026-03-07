from typing import Callable, Dict
from .interface import LLMClient


class LLMFactory:
    _registry: Dict[str, Callable[..., LLMClient]] = {}

    @classmethod
    def register(cls, provider: str, creator: Callable[..., LLMClient]):
        cls._registry[provider] = creator

    @classmethod
    def create(cls, provider: str, **kwargs) -> LLMClient:
        if provider not in cls._registry:
            raise ValueError(
                f"Unsupported provider: {provider}",
                f"Available providers: [{', '.join(cls._registry.keys())}]",
            )

        return cls._registry[provider](**kwargs)
