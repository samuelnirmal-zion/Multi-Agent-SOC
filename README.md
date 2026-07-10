# Multi-Agent-SOC

This project provides a lightweight SOC assistant that analyzes security events and returns an initial response through a coordinator agent.

## Run locally

1. Activate the virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Start the app:
   `python app.py`

## Notes

- The app uses a Groq-backed coordinator when a valid `GROQ_API_KEY` is available.
- If the API key is missing or the dependency is unavailable, the app falls back to a local response so the CLI still works.
