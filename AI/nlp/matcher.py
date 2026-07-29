from spacy.matcher import Matcher

from AI.nlp.patterns import (
    NOTE_PATTERNS,
    REMINDER_PATTERNS,
    MEMORY_PATTERNS,
)


class JARVISMatcher:

    def __init__(self, nlp):
        self.matcher = Matcher(nlp.vocab)
        self._register_patterns()

    def _register_patterns(self):
        pattern_groups = [
            NOTE_PATTERNS,
            REMINDER_PATTERNS,
            MEMORY_PATTERNS,
        ]

        for group in pattern_groups:
            for intent, patterns in group.items():
                self.matcher.add(intent, patterns)

    def match(self, doc):
        return self.matcher(doc)