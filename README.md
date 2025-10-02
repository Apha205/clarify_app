# Clarify

Clarify is a desktop-first reading assistant that helps users scan, read, and understand documents. It provides OCR for PDFs and images, real-time text-to-speech reading with highlighted words, and optional summaries or explanations when connected to an external API key supplied by the user(BYOK). The application is designed to run locally, keeping documents and notes private.

## Features

- **OCR Processing**: Extract text from PDFs (text-based or scanned)
- **Text-to-Speech**: Generate real-time audio streams, including optional word-level timing markers.
- **Summarization**: Optional LLM-based summaries using user-provided API keys (e.g., OpenAI).
- **Notes Management**: CRUD operations for user notes linked to documents or pages.
- **Local-First**: All processing is local by default; data stays on the user's machine.

## Tech Stack

- **Backend**: Python, FastAPI
- **Frontend**: Building...
- **Database**: PostgreSQL (local)
- **OCR**: PyMuPDF, pytesseract
- **TTS**: pyttsx3 (Currently)
- **ORM**: SQLAlchemy


## Privacy

Clarify prioritizes user privacy by running entirely locally. Documents, notes, and processing remain on the user's device. External API calls for summarization require explicit user-provided keys.