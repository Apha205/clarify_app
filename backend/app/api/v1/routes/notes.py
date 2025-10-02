from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.services.db_service import create_note, get_notes_for_document, update_note, delete_note

router = APIRouter()

class NoteCreate(BaseModel):
    document_id: int
    page_id: int = None
    content: str

class NoteUpdate(BaseModel):
    content: str

@router.post("/notes")
def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = create_note(db, note.document_id, note.page_id, note.content)
    return {"note_id": new_note.id, "message": "Note created"}

@router.get("/notes/{doc_id}")
def get_notes(doc_id: int, db: Session = Depends(get_db)):
    notes = get_notes_for_document(db, doc_id)
    return [{"id": n.id, "document_id": n.document_id, "page_id": n.page_id, "content": n.content, "created_at": n.created_at} for n in notes]

@router.put("/notes/{note_id}")
def update_note_endpoint(note_id: int, note_update: NoteUpdate, db: Session = Depends(get_db)):
    updated_note = update_note(db, note_id, note_update.content)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note updated"}

@router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    success = delete_note(db, note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}