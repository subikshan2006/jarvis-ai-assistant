import pyautogui

def control_mouse_keyboard(command):
    command = command.lower()

    if "move mouse" in command:
        try:
            parts = command.replace("move mouse", "").strip().split()
            x = int(parts[0])
            y = int(parts[1])
            pyautogui.moveTo(x, y)
            return f"Moved mouse to {x}, {y}."
        except:
            return "Failed to move mouse. Say: move mouse [x] [y]"

    elif "click" in command:
        if "right" in command:
            pyautogui.click(button='right')
            return "Right click done."
        else:
            pyautogui.click()
            return "Left click done."

    elif "double click" in command:
        pyautogui.doubleClick()
        return "Double click done."

    elif "type" in command:
        text = command.replace("type", "").strip()
        pyautogui.write(text)
        return f"Typed: {text}"

    elif "press enter" in command:
        pyautogui.press('enter')
        return "Pressed Enter."

    elif "press escape" in command:
        pyautogui.press('esc')
        return "Pressed Escape."

    elif "scroll up" in command:
        pyautogui.scroll(500)
        return "Scrolled up."

    elif "scroll down" in command:
        pyautogui.scroll(-500)
        return "Scrolled down."

    return None
