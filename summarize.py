from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model_name = "flan-t5-small"
model_name = "bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline("summarization", model = model, tokenizer = tokenizer, max_length=250, min_length=10)

# res = summarizer("sentiment analysis can be considered a form of sequence classification. In sentiment analysis, the goal is to classify a piece of text (which can be considered a sequence of words or tokens) into predefined categories or classes representing different sentiments, such as positive, negative, or neutral. Sequence classification, in a broader sense, refers to the task of assigning a label or category to a sequence of input data. This sequence could be a text sequence (as in sentiment analysis), a sequence of audio samples (as in speech recognition), or a sequence of video frames (as in action recognition). Sentiment analysis is a specific application of sequence classification where the input sequence is a piece of text, and the task is to classify it into different sentiment categories. In the context of natural language processing (NLP) and machine learning, sentiment analysis is often treated as a sequence classification problem, and techniques such as recurrent neural networks (RNNs), convolutional neural networks (CNNs), or transformer-based models like BERT or RoBERTa are commonly used to solve it. These models are trained to classify sequences of tokens (words or subwords) into different classes, where each class represents a sentiment category.")

# print(res)

