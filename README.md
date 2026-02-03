# article-summarizer

Minimal project scaffold with pseudocode for a 2-hour MVP article summarizer.

## Structure
- `backend/server.js` – backend API pseudocode
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

## Notes
- This is pseudocode only. Replace the placeholders with real code and wire to OpenAI.
- Set `OPENAI_API_KEY` in the backend environment when implementing.