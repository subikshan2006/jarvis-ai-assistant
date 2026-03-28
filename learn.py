import os
import fitz  # PyMuPDF
import json
from memory import remember, load_memory
from llama_cpp import Llama

llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

MEMORY_FILE = "jarvis_memory.json"

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        return "File not found."

    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"Failed to read PDF: {str(e)}"

def learn_from_file(file_path):
    if file_path.endswith(".pdf"):
        content = extract_text_from_pdf(file_path)
    elif file_path.endswith(".txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            return "Error reading TXT file."
    else:
        return "Unsupported file type."

    if not content:
        return "Couldn't read anything from the file."

    # Save content to memory by file name
    remember(f"file:{os.path.basename(file_path)}", content[:5000])  # store first 5K chars
    return "File content learned and saved."

def ask_about_file(file_name, question):
    memory = load_memory()
    file_key = f"file:{file_name}"
    content = memory.get(file_key)

    if not content:
        return "I haven't learned that file yet. Please say: 'Learn file ...' first."

    # Ask LLaMA with file content + question
    prompt = f"""
You are Jarvis, an assistant with file memory. Here is the content from a file named {file_name}:
---
{content}
---
Now answer this user question based only on the content above:
Q: {question}
A:"""

    response = llm(prompt=f"[INST] {prompt} [/INST]", max_tokens=300, stop=["</s>"])
    return response["choices"][0]["text"].strip()
