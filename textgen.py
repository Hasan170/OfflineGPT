from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text_gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=100, min_length=10)

# res = text_gen("Do you know about Java?")

# print(res)