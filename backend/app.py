# backend/app.py
# Author: Mohamed Hassan
# This is the main file for the article summarizer application

#importing the necessary libraries
from fastapi import FastAPI, HTTPException
from summarizer import summarize_text
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests

#creating the FastAPI app
app = FastAPI()

#creating the summarizeRequest model to validate the request
class summarizeRequest(BaseModel):
    url:str | None = None
    text:str | None = None

#creating the summarize endpoint
@app.post("/summarize")
#creating the summarize function to summarize the text 
def summarize(request: summarizeRequest):
    #validating the request
    if(request.url and request.text) or (not request.url and not request.text):
        #raising an error if the request is invalid -> can only provide one of URL or text, not both or none
        raise HTTPException(status_code=400, detail="You can only provide one of URL or text")
    #if the URL is provided, fetch the content from the URL
    if request.url:
        try:
            #fetching the content from the url
            html = requests.get(request.url).text
            #parsing the html content
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
    #summarizing the text
    summary = summarize_text(content)
    #returning the summary
    return {"summary": summary}