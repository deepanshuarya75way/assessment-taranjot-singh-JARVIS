class KeywordExtractor:
    """Extracts meaningful keywords from a spaCy Doc."""

    def extract(self, doc):
        """
        Extract normalized keywords from a processed spaCy Doc.
        """

        keywords = []

        for token in doc:

            if token.is_stop:
                continue

            if token.is_punct:
                continue

            if token.is_space:
                continue

            if not token.is_alpha:
                continue

            keyword = token.lemma_.lower()

            if keyword not in keywords:
                keywords.append(keyword)

        return keywords