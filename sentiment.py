from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

sentiment_analyzer = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)

res = sentiment_analyzer("I love you")

print(res)

