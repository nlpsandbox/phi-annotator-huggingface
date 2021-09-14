import os
from transformers import AutoModelForTokenClassification as amc, AutoTokenizer as at


MODEL_NAME = os.getenv('HUGGINGFACE_MODEL', 'dslim/bert-base-NER')
LOCAL_DIRECTORY = 'hf'

tokenizer = at.from_pretrained(MODEL_NAME)
tokenizer.save_pretrained(LOCAL_DIRECTORY)

model = amc.from_pretrained(MODEL_NAME)
model.save_pretrained(LOCAL_DIRECTORY)
