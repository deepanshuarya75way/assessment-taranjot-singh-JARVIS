from AI.nlp.nlp_processor import NLPProcessor

processor = NLPProcessor()
doc = processor.process("This is a sample text for NLP processing.")

print("Tokens:" , [token.text for token in doc])
print("Named Entities:", [(ent.text, ent.label_) for ent in doc.ents])
print("Part-of-Speech Tags:", [(token.text, token.pos_) for token in doc])
print("Lemmatization:", [(token.text, token.lemma_) for token in doc])
