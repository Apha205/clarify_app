from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.services.summarize_service import summarize_text
from app.services.db_service import create_summary

router = APIRouter()

class SummarizeRequest(BaseModel):
    doc_id: int
    text: str
    api_key: str
    page_id: int = None

@router.post("/summarize")
def summarize(request: SummarizeRequest, db: Session = Depends(get_db)):
    summary_text = summarize_text(request.text, request.api_key)
    summary = create_summary(db, request.doc_id, request.page_id, summary_text, request.api_key)
    return {"summary_id": summary.id, "summary": summary_text}