from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

summary = summarizer("Hello, how are you?", max_length=130, min_length=30, do_sample=False)
print(summary)
