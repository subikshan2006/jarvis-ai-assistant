import json
import os

MEMORY_FILE = "jarvis_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key.lower()] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key.lower(), None)

def add_to_autolearning_history(question, answer):
    memory = load_memory()
    history = memory.get("auto_learning", [])
    history.append({"q": question, "a": answer})
    memory["auto_learning"] = history[-50:]  # Keep last 50 only
    save_memory(memory)

def get_autolearning_memory():
    memory = load_memory()
    return memory.get("auto_learning", [])
