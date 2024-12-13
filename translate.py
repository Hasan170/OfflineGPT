from transformers import pipeline
from transformers import MBartTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBartTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

translator = pipeline("translation", model=model, tokenizer=tokenizer, src_lang='en_XX', tgt_lang='hi_IN')

# res = translator("My name is George")

# print(res)
