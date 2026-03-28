# 🤖 JARVIS AI Assistant — Advanced Offline AI System

JARVIS is a fully offline, modular AI assistant built using Python.
Inspired by Iron Man’s JARVIS, this system integrates voice interaction, automation, computer vision, and intelligent task execution into one unified assistant.

This project demonstrates real-world AI engineering skills including system design, modular architecture, and multi-domain integration.

---

# 🚀 Key Highlights

* Fully offline AI assistant (privacy-focused)
* Voice-controlled system
* Modular architecture (easy to scale)
* Computer vision + OCR support
* Face authentication security
* File learning & memory system
* YouTube transcript intelligence
* System automation (apps, keyboard, mouse)
* Web search integration

---

# 🧠 System Architecture

The system follows a modular pipeline:

1. Wake Listener → Activates assistant
2. Voice Input → Converts speech to text
3. Intent Router → Understands user command
4. Brain Module → Decides action
5. Execution Modules → Perform task
6. Voice Output → Responds to user

---

# 📁 Project Structure

jarvis-ai-assistant/

Core:

* main.py                → Entry point
* brain.py               → Core logic
* intent_router.py       → Command routing

Memory:

* memory.py
* learn.py

Voice:

* voice_input.py
* voice_output.py
* wake_listener.py

Vision:

* image_reader.py
* screenshot_tool.py

System:

* system_control.py
* system_status.py
* app_launcher.py

Automation:

* input_controller.py

Security:

* face_auth.py

File Handling:

* file_manager.py
* pdf_reader.py

Web:

* web_search.py
* youtube_learner.py

Utilities:

* cleanup.py
* reminder.py

Other:

* requirements.txt
* README.md

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

git clone https://github.com/subikshan2006/jarvis-ai-assistant.git
cd jarvis-ai-assistant

---

## Step 2: Create Virtual Environment (Recommended)

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

---

## Step 3: Install Dependencies

pip install -r requirements.txt

---

## Step 4: Install External Tools

Install Tesseract OCR (for image reading)
Download: https://github.com/tesseract-ocr/tesseract

If needed, set path in code:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

---

Install PyAudio (if error occurs):

pip install pipwin
pipwin install pyaudio

---

## Step 5: Run JARVIS

python main.py

---

# 🎯 Features Explained

Voice System:

* Converts speech to text
* Responds using text-to-speech
* Continuous listening

Brain & Intent System:

* Processes commands
* Routes to modules
* Easily extendable

Face Authentication:

* Uses webcam to verify user
* Adds security

Vision System:

* OCR (extract text from images)
* Screenshot capture

File Intelligence:

* Reads PDFs
* Extracts content
* Stores knowledge

Web & YouTube:

* Web search
* YouTube transcript learning

System Automation:

* Open apps
* Control system
* Automate tasks

Reminder System:

* Set reminders
* Execute tasks

---

# 💻 Example Commands

* Open YouTube
* What is the time
* Take a screenshot
* Read this PDF
* Search for AI news
* Remind me at 6 PM
* Shutdown system

---

# 🧩 Working Flow

User → Voice Input → Intent Detection → Brain → Module Execution → Voice Output

---

# ⚠️ Important Notes

* Best on Windows
* Requires microphone
* Webcam needed for face authentication
* Some features need internet

---

# 🔧 Customization Guide

To add new command:
Edit intent_router.py

To add new feature:
Create new module → connect to brain

---

# 🔥 Future Improvements

* Local LLM (llama.cpp)
* GUI interface
* Mobile app
* Smart memory (vector database)
* Emotion detection

---

# 📸 Demo

(Add screenshots here)
(Add demo video link here)

---

# 👨‍💻 Author

Subikshan P
B.Tech Artificial Intelligence and Machine Learning
Saveetha Engineering College

Email: [subikshan182006@gmail.com](mailto:subikshan182006@gmail.com)
GitHub: https://github.com/subikshan2006

---

# ⭐ Support

If you like this project:
Give it a star on GitHub
Share with others

---

# 🏁 Conclusion

JARVIS is a complete AI system combining voice AI, automation, computer vision, and intelligent processing into one unified assistant.
It showcases practical, real-world AI engineering skills suitable for production-level applications.
