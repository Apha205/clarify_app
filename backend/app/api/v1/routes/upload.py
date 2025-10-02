from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.db_service import create_document, create_page
from app.services.ocr_service import extract_text_from_pdf
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.lower().endswith('.pdf'):
        return {"error": "Only PDF files are allowed"}
    
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Save document to DB
    doc = create_document(db, file.filename, filepath)
    
    # Extract text and save pages
    pages_data = extract_text_from_pdf(filepath)
    for page_data in pages_data:
        create_page(db, doc.id, page_data["page"], page_data["text"], page_data["positions"])
    
    return {"document_id": doc.id, "message": "Document uploaded and processed successfully"}