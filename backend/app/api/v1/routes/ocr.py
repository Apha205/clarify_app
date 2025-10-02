from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.db_service import get_pages_for_document

router = APIRouter()

@router.get("/ocr/{doc_id}")
def get_ocr_data(doc_id: int, db: Session = Depends(get_db)):
    pages = get_pages_for_document(db, doc_id)
    return [
        {
            "page": page.page_number,
            "text": page.text,
            "positions": page.positions
        }
        for page in pages
    ]