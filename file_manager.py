import os
import pyautogui
import subprocess

def list_files_in_folder(path):
    if not os.path.exists(path):
        return "That folder doesn't exist."
    
    files = os.listdir(path)
    if not files:
        return "The folder is empty."
    
    return "Files in folder:\n" + "\n".join(files)

def open_file(file_path):
    if not os.path.exists(file_path):
        return "File not found."
    try:
        os.startfile(file_path)
        return f"Opened {os.path.basename(file_path)}."
    except Exception as e:
        return f"Couldn't open file: {str(e)}"

def delete_file(file_path):
    if not os.path.exists(file_path):
        return "File doesn't exist."
    try:
        os.remove(file_path)
        return f"Deleted {os.path.basename(file_path)}."
    except Exception as e:
        return f"Failed to delete file: {str(e)}"
