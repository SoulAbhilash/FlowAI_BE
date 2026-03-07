from typing import Type

from annotated_types import T
from google import genai
from google.genai import errors
import asyncio

from ai_tools.app.llm.interface import LLMClient
from ai_tools.app.llm.factory import register


@register("gemini")
class GeminiClient(LLMClient):
    provider_name = "gemini"

    def __init__(self, api_key: str, model: str, retries: int = 3):
        if not api_key:
            raise ValueError("Gemini requires an api_key")

        if not model:
            raise ValueError("Gemini requires a model name")

        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.retries = retries

    async def generate(self, prompt: str, response_schema: Type[T]) -> Type[T]:
        response_schema_json = response_schema.model_json_schema()
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        last_error = None

        for attempt in range(self.retries):
            try:
                response = await self.client.aio.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json",
                        "response_json_schema": response_schema_json,
                    },
                )

                # Validate response structure
                if not response:
                    raise RuntimeError("Empty response from Gemini")

                text = getattr(response, "text", None)

                if not text:
                    raise RuntimeError("Gemini returned no text")

                return text.strip()

            # API key issues
            except errors.PermissionDenied as e:
                raise RuntimeError("Invalid Gemini API key") from e

            # Rate limit
            except errors.ResourceExhausted as e:
                last_error = e
                await asyncio.sleep(2**attempt)

            # Bad request / invalid model
            except errors.InvalidArgument as e:
                raise RuntimeError(f"Invalid Gemini request: {e}") from e

            # Server side issues
            except errors.InternalServerError as e:
                last_error = e
                await asyncio.sleep(2**attempt)

            # Network errors
            except Exception as e:
                last_error = e
                await asyncio.sleep(2**attempt)

        raise RuntimeError(
            f"Gemini request failed after {self.retries} retries"
        ) from last_error
