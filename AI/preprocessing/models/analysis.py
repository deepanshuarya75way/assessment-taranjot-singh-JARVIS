from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AnalysisResult:
    """
    Represents the complete NLP analysis of a user request.

    Produced by the RequestAnalyzer and consumed by the
    Orchestrator to determine how the request should be
    processed.
    """

    # Original user input
    user_prompt: str

    # Detected intent (None if no intent matched)
    intent: str | None = None

    # Whether Gemini should handle the request
    needs_llm: bool = True

    # Confidence of the detected intent
    confidence: float = 0.0

    # Parsed spaCy document
    doc: Any | None = None

    # Structured entities extracted by the EntityExtractor
    entities: dict[str, Any] = field(default_factory=dict)

    # Normalized keywords extracted from the prompt
    keywords: list[str] = field(default_factory=list)