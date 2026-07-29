import spacy


class NLPProcessor:
    """
    Loads the spaCy language model and converts
    raw text into a spaCy Doc object.
    """

    def __init__(self, model_name="en_core_web_sm"):
        self.model_name = model_name
        self.nlp = spacy.load(model_name)

    def process(self, text):
        """
        Convert raw text into a spaCy Doc.
        """

        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        text = text.strip()

        if not text:
            raise ValueError("Input text cannot be empty.")

        return self.nlp(text)