# backend/summarizer.py
# Author: Mohamed Hassan
# This is the summarizer module for the article summarizer application

#importing the summarizer pipeline
from transformers import pipeline

#making the summarizer pipeline
summarizer = pipeline("summarization", model = "facebook/bart-large-cnn")

#the summarize function summarizes the text using the summarizer pipeline and returns the summary
def summarize(text : str) -> str:
    #stripping text of any extra spaces
    text = text.strip()
    #summarizing the text using the pipeline
    result = summarizer(text, max_length = 130, min_length = 30, do_sample = False)
    #returning the summary in the format of a string
    return result[0]['summary_text']
