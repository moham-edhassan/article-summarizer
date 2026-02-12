# backend/app.py
# Author: Mohamed Hassan
# This is the main file for the article summarizer application

#importing the necessary libraries
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from readability import Document
from summarizer import summarize
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests

#creating the FastAPI app
app = FastAPI()

#adding the CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    #allowing the frontend to access the backend from the localhost port 5500
    allow_origins=["https://artsummarizer.netlify.app"],
    allow_credentials=True,
    #allowing all methods and headers
    allow_methods=["*"],
    allow_headers=["*"],
)

#creating the summarizeRequest model to validate the request
class summarizeRequest(BaseModel):
    url:str | None = None
    text:str | None = None

#creating the summarize endpoint
@app.post("/summarize")
#creating the summarize function to summarize the text 
def summarize_endpoint(request: summarizeRequest):
    #validating the request
    if(request.url and request.text) or (not request.url and not request.text):
        #raising an error if the request is invalid -> can only provide one of URL or text, not both or none
        raise HTTPException(status_code=400, detail="You can only provide one of URL or text")
    #if the URL is provided, fetch the content from the URL
    if request.url:
        try:
            #fetching the content from the url with a timeout of 10 seconds
            html = requests.get(request.url, timeout=10).text
            #parsing the html content using the readability library
            document = Document(html)
            #getting the summary of the article
            html = document.summary()
            #parsing the html content using the beautifulsoup library
            soup = BeautifulSoup(html, "html.parser")
            #removing the script and style tags
            for tag in soup(["script", "style"]):
                #extracting the text from the script and style tags
                tag.extract()
            #getting the text from the soup, and stripping the extra spaces
            content = soup.get_text(" ", strip=True)
        #raising an error if the content is not fetched
        except Exception as e:
            
            raise HTTPException(status_code=500, detail=f"Error fetching content from URL: {e}")
    #if the text is provided, use the text
    else:
        #using the text input
        content = request.text
    #trying to summarize the text
    try:
        summary = summarize(content)
        #raising an error if the summary is not a string
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    #returning the summary
    return {"summary": summary}