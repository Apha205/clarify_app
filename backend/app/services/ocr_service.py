import fitz
import io
from PIL import Image
import pytesseract

def extract_text_from_pdf(filepath: str) -> list[dict]:
    doc = fitz.open(filepath)
    result = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        positions = None
        if text.strip():
            # Has text layer, extract positions
            dict_data = page.get_text("dict")
            words = []
            for block in dict_data["blocks"]:
                if block["type"] == 0:  # text block
                    for line in block["lines"]:
                        for span in line["spans"]:
                            words.append({
                                "word": span["text"],
                                "bbox": span["bbox"]
                            })
            positions = words
        else:
            # Scanned, use OCR
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            text = pytesseract.image_to_string(img)
            positions = None  # OCR doesn't provide positions easily
        result.append({
            "page": page_num + 1,
            "text": text,
            "positions": positions
        })
    doc.close()
    return result