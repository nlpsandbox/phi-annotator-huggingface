from transformers import AutoModelForTokenClassification as amc, AutoTokenizer as at


tokenizer = at.from_pretrained('dslim/bert-base-NER')
tokenizer.save_pretrained('dslim-tokenizer')

model = amc.from_pretrained('dslim/bert-base-NER')
model.save_pretrained('dslim-model')
