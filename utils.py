import docx
import fitz
from io import BytesIO

def extract_text_from_pdf(file_obj):
    doc = fitz.open(stream=file_obj.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file_obj):
    doc = docx.Document(file_obj)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_txt(file_obj):
    text = file_obj.read().decode('utf-8')
    return text

def extract_text(uploaded_file):
    uploaded_file.seek(0)
    
    file_name = uploaded_file.name.lower()
    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    elif file_name.endswith(".txt"):
        return extract_text_from_txt(uploaded_file)
    else:
        return "Unsupported file format."