from AI.config.gemini_config import GeminiConfig
from AI.clients.gemini_client import GeminiClient


def main():
    config = GeminiConfig()
    client = GeminiClient(config)

    

    prompt = "Hello Gemini! Please introduce yourself in two sentences."

    print(f"API Key Loaded: {config.api_key[:10]}...")
    print(f"Using model: {config.model_name}")

    response = client.generate(prompt)

    print("Prompt:")
    print(prompt)
    print("\nResponse:")
    print(response)


if __name__ == "__main__":
    main()