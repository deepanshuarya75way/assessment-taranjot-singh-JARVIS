from AI.preprocessing.models.intent import Intent


class IntentDetector:
    """Determines the user's intent from matcher results."""

    def __init__(self, nlp, matcher):
        self.nlp = nlp
        self.matcher = matcher

    def detect(self, doc):
        """
        Determine the most appropriate intent for a spaCy Doc.
        """
        matches = self.matcher.match(doc)

        if not matches:
            return None

        match_id, start, end = max(
            matches,
            key=lambda match: match[2] - match[1]
        )

        intent_name = self.nlp.vocab.strings[match_id]

        try:
            return Intent[intent_name]
        except KeyError:
            return None