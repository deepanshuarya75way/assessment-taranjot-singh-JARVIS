from google import genai
from AI.config.gemini_config import GeminiConfig

config = GeminiConfig()

client = genai.Client(api_key=config.api_key)

for model in client.models.list():
    print(model.name)