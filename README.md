# article-summarizer

## Structure
- `backend/server.js` 
- `backend/package.json` – backend scripts
- `frontend/index.html` – simple UI shell
- `frontend/app.js` – frontend pseudocode

## Pseudocode Summary

```
Frontend:
  - User inputs URL or raw text
  - POST { url, text } to /summarize
  - Render summary or error

Backend:
  - Validate input
  - If url: fetch HTML + extract main text
  - Call OpenAI summarization API
  - Return summary
```
