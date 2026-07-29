from AI.nlp.nlp_processor import NLPProcessor
from AI.nlp.matcher import JARVISMatcher
from AI.nlp.intent_detector import IntentDetector
from AI.nlp.entity_extractor import EntityExtractor
from AI.nlp.keyword_extractor import KeywordExtractor
from AI.preprocessing.models.analysis import AnalysisResult


class RequestAnalyzer:
    """
    Coordinates the NLP pipeline and produces a complete AnalysisResult.
    """

    def __init__(self):
        self.processor = NLPProcessor()
        self.matcher = JARVISMatcher(self.processor.nlp)
        self.intent_detector = IntentDetector(
            self.processor.nlp,
            self.matcher,
        )
        self.entity_extractor = EntityExtractor()
        self.keyword_extractor = KeywordExtractor()

    def analyze(self, prompt: str) -> AnalysisResult:
        """
        Analyze a user prompt and return the complete NLP analysis.
        """

        # Ignore empty prompts
        if not prompt or not prompt.strip():
            return AnalysisResult(
                user_prompt=prompt,
                needs_llm=False,
                confidence=0.0,
            )

        # Process text
        doc = self.processor.process(prompt)

        # Detect intent
        intent = self.intent_detector.detect(doc)

        # Extract entities
        entities = self.entity_extractor.extract(
            intent,
            doc,
        )

        # Extract keywords
        keywords = self.keyword_extractor.extract(doc)

        # Determine whether Gemini is required
        needs_llm = intent is None
        confidence = 0.0 if needs_llm else 1.0

        # Build final analysis
        return AnalysisResult(
            user_prompt=prompt,
            intent=intent,
            needs_llm=needs_llm,
            confidence=confidence,
            doc=doc,
            entities=entities,
            keywords=keywords,
        )