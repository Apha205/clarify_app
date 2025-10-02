from sqlalchemy.orm import Session
from ..db.models import Document, Page, Note, Summary

def create_document(db: Session, filename: str, filepath: str) -> Document:
    doc = Document(filename=filename, filepath=filepath)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def get_document(db: Session, doc_id: int) -> Document:
    return db.query(Document).filter(Document.id == doc_id).first()

def create_page(db: Session, document_id: int, page_number: int, text: str, positions: dict = None) -> Page:
    page = Page(document_id=document_id, page_number=page_number, text=text, positions=positions)
    db.add(page)
    db.commit()
    db.refresh(page)
    return page

def get_pages_for_document(db: Session, doc_id: int) -> list[Page]:
    return db.query(Page).filter(Page.document_id == doc_id).all()

def create_note(db: Session, document_id: int,content: str, page_id: int = None ) -> Note:
    note = Note(document_id=document_id, page_id=page_id, content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes_for_document(db: Session, doc_id: int) -> list[Note]:
    return db.query(Note).filter(Note.document_id == doc_id).all()

def update_note(db: Session, note_id: int, content: str) -> Note:
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        note.content = content
        db.commit()
        db.refresh(note)
    return note

def delete_note(db: Session, note_id: int) -> bool:
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
        return True
    return False

def create_summary(db: Session, document_id: int, summary_text: str, page_id: int = None, api_key_used: str = None) -> Summary:
    summary = Summary(document_id=document_id, page_id=page_id, summary_text=summary_text, api_key_used=api_key_used)
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary

def get_summaries_for_document(db: Session, doc_id: int) -> list[Summary]:
    return db.query(Summary).filter(Summary.document_id == doc_id).all()