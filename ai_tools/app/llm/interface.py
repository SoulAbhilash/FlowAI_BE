from typing import Protocol
from typing import Type

from annotated_types import T


class LLMClient(Protocol):
    async def generate(self, prompt: str, response_schema: Type[T]) -> Type[T]: ...
