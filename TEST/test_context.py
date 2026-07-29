from AI.orchestration.context_builder import ContextBuilder

builder = ContextBuilder()

print(
    builder.build_context(
        "Hello Jarvis!"
    )
)