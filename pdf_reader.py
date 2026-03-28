import fitz  # PyMuPDF
from memory import remember

def extract_pdf_text(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def summarize_text(text):
    lines = text.splitlines()
    lines = [line.strip() for line in lines if len(line.strip()) > 40]
    summary = "\n".join(lines[:5]) if len(lines) >= 5 else "\n".join(lines)
    return summary or "The document appears to be empty."

def learn_pdf(file_path, topic_name="document"):
    full_text = extract_pdf_text(file_path)
    if "Error" in full_text:
        return full_text

    remember(topic_name, full_text[:1000])  # Store first 1000 chars
    summary = summarize_text(full_text)
    return f"I’ve learned from {file_path}.\nHere's a quick summary:\n{summary}"
