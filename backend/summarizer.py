# backend/summarizer.py
# Author: Mohamed Hassan
# This is the summarizer module for the article summarizer application
#importing necessary libraries
import requests
import os
#setting the API token and model URL
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
#setting the model URL
HF_MODEL_URL = "https://router.huggingface.co/hf-inference/models/sshleifer/distilbart-cnn-12-6"

#the summarize function summarizes the text using the summarizer pipeline and returns the summary
def summarize(text: str) -> str:
    #setting the headers for the request
    if not HF_API_TOKEN:
        raise ValueError("HF_API_TOKEN is not set")
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    #setting the payload for the request
    payload = {
        "inputs": text[:4500],
        "parameters": {"max_length": 170, "min_length": 120, "do_sample": False}
    }
    #sending the request to the model and getting the response
    res = requests.post(HF_MODEL_URL, headers=headers, json=payload, timeout=60)
    #raising an error if the request fails
    res.raise_for_status()
    #getting the data from the response
    data = res.json()
    #raising an error if the response is not a dictionary
    if isinstance(data, dict):
        raise ValueError(data.get("error", "Unexpected response from model"))
    #raising an error if the response is not a list
    if not data or "summary_text" not in data[0]:
        raise ValueError("No summary returned from model")
    #returning the summary in the format of a string
    return data[0]["summary_text"]
