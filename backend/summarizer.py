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
    #setting the max characters to 3000
    max_characters = 3000
    #if the text is long than 3000 chars, truncate the text to 3000 chars
    if len(text) > max_characters:
        #truncating the text to 3000 chars
        text = text[:max_characters]
        
    #setting the max length to 130
    max_length = 130
    #setting the min length to 30
    min_length = 30
    #if the text is less than 400 chars, set the min length to 10
    if len(text) < 400:
        #setting the min length to 10
        min_length = 10
    #summarizing the text using the pipeline
    result = summarizer(text, max_length = max_length, min_length = min_length, do_sample = False)
    #returning the summary in the format of a string
    return result[0]['summary_text']
