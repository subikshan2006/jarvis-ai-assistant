import pytesseract
from PIL import Image
import os

# Optional: Set this if tesseract is not in PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        return "Image file not found."
    
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Failed to read image: {e}"
