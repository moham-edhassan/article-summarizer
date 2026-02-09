# Article Summarizer

A web app that summarizes either a URL or raw text using Hugging Face’s `facebook/bart-large-cnn` model. The backend is built with FastAPI and the frontend is a lightweight HTML/CSS/JS page.

## Tech Stack

- Frontend: HTML, CSS, Vanilla JavaScript
- Backend: FastAPI (Python)
- NLP: Hugging Face Transformers (`facebook/bart-large-cnn`)
- Utilities: Requests, BeautifulSoup

## Features

- Summarize articles from a URL
- Summarize raw text input
- Loading state and error handling
- Clean, minimal UI

## Run Steps

1. Install backend dependencies:
   cd backend
   pip install -r requirements.txt

2. Start the API:
   uvicorn app:app --reload

3. Open the frontend:
   - Open `frontend/index.html` in your browser


## API Usage

POST /summarize

Example request body:
{
  "text": "Paste article text here..."
}

Example response:
{
  "summary": "..."
}

## File Structure

article-summarizer/
├── backend/
│   ├── app.py
│   ├── summarizer.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── README.md
├── LICENSE
└── .gitignore
  
## Next Steps: 

- Adding PDF upload support -> Adding this feature next
- Improving article extraction -> Will be challenging
- Adding tests and input length handling -> Limit length of article length
- Deploying the web app