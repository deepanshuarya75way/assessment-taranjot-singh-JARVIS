from google import genai

from AI.config.gemini_config import GeminiConfig


class GeminiClient:

    def __init__(self, config: GeminiConfig):

        self.config = config

        self.client = genai.Client(
            api_key=self.config.api_key
        )

    def generate(self, prompt: str) -> str:
        """Send a prompt to Gemini and return the generated text."""
        try:
            response = self.client.models.generate_content(
                model=self.config.model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            raise RuntimeError(
                f"Failed to generate response from Gemini: {e}"
            ) from e