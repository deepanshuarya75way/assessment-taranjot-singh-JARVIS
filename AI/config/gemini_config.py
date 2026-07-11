import os
from dotenv import load_dotenv

load_dotenv()


class GeminiConfig:

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.5-flash"
        ).strip()

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please add it to your .env file."
            )

        if not self.model_name:
            raise ValueError(
                "GEMINI_MODEL not found. Please add it to your .env file."
            )