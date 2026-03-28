from llama_cpp import Llama

llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

PERSONALITY = (
    "You are Jarvis, a helpful and intelligent AI created by Subikshan. "
    "You are confident, friendly, and witty like Iron Man's assistant. "
    "You answer clearly, briefly, and with a bit of charm when appropriate."
)

def ask_brain(question):
    prompt = f"[INST] {PERSONALITY}\nUser: {question}\nJarvis: [/INST]"
    output = llm(prompt=prompt, max_tokens=300, stop=["</s>"])
    return output["choices"][0]["text"].strip()
