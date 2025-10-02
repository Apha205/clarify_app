from fastapi import APIRouter
from .routes import upload, ocr, tts, summary, notes

api_router = APIRouter()

api_router.include_router(upload.router, tags=["upload"])
api_router.include_router(ocr.router, tags=["ocr"])
api_router.include_router(tts.router, tags=["tts"])
api_router.include_router(summary.router, tags=["summary"])
api_router.include_router(notes.router, tags=["notes"])