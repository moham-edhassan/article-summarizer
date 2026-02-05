## Project: An article summarizer that either takes a URL or raw text as input. Uses HuggingFace's facebook-bart summarization model, which it then parses the input and returns a summary.

## Tech Stack
- Frontend: HTML, CSS, Vanilla JavaScript
- Backend: FastAPI (Python)
- Summarization: Hugging Face Transformers (`facebook/bart-large-cnn`)
- Utilities: Requests, BeautifulSoup

## Features
- Summarize articles from a URL
- Summarize raw text input
- Simple error handling and loading state
- Clean, minimal UI

## Run Steps
1. Install backend dependencies:
    cd backend
    pip install -r requirements.txt
   
2. Start the API:
    uvicorn app:app --reload

3. Open the frontend:
   - Open `frontend/index.html` in your browser


## Plans for this project:
- Will allow for PDF upload
- Improve article extraction(next step)
- Adding tests and input length handling(Can't allow for extremely long inputs)
- Deploy it 

## File structure:
article-summarizer/
  backend/
    app.py
    summarizer.py
    requirements.txt
  frontend/
    index.html
    app.js
    style.css
  README.md
  LICENSE
  .gitignore