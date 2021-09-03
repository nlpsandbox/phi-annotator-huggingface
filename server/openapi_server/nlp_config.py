from transformers import AutoTokenizer as at
from transformers import AutoModelForTokenClassification as amc, pipeline


class Bert:
    def __init__(self):
        self.tokenizer = at.from_pretrained("dslim-tokenizer")
        self.model = amc.from_pretrained("dslim-model")
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def get_entities(self, sample_text, label):
        ner_results = self.nlp(sample_text)
        ner_results = [r for r in ner_results if label in r['entity']]
        return ner_results


bert = Bert()
