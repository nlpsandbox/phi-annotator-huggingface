from transformers import AutoTokenizer as at
from transformers import AutoModelForTokenClassification as amc, pipeline


class Bert:
    def __init__(self) -> None:
        self.tokenizer = None
        self.model = None
        self.nlp = None

    def initialize(self):
        self.tokenizer = at.from_pretrained("./dslim-bert/tokenizer")
        self.model = amc.from_pretrained("./dslim-bert/model")
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer)

    def get_entities(self, sample_text, label):
        if self.nlp is None:
            self.initialize()
        ner_results = self.nlp(sample_text)
        ner_results = [r for r in ner_results if label in r['entity']]
        return ner_results


bert = Bert()
