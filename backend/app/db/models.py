from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    pages = relationship("Page", back_populates="document")
    notes = relationship("Note", back_populates="document")
    summaries = relationship("Summary", back_populates="document")

class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    page_number = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    positions = Column(JSON, nullable=True)  # List of dicts: [{"word": "text", "bbox": [x0,y0,x1,y1]}]

    document = relationship("Document", back_populates="pages")
    notes = relationship("Note", back_populates="page")
    summaries = relationship("Summary", back_populates="page")

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    page_id = Column(Integer, ForeignKey("pages.id"), nullable=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="notes")
    page = relationship("Page", back_populates="notes")

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    page_id = Column(Integer, ForeignKey("pages.id"), nullable=True)
    summary_text = Column(Text, nullable=False)
    api_key_used = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="summaries")
    page = relationship("Page", back_populates="summaries")