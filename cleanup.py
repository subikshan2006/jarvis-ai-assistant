import os
import shutil
import time
from send2trash import send2trash
from datetime import datetime

def cleanup_downloads(days_old=7):
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    deleted = 0
    if os.path.exists(downloads):
        for file in os.listdir(downloads):
            path = os.path.join(downloads, file)
            if os.path.isfile(path):
                age_days = (time.time() - os.path.getmtime(path)) / 86400
                if age_days > days_old:
                    try:
                        send2trash(path)
                        deleted += 1
                    except:
                        pass
    return f"🧹 Cleaned {deleted} old files from Downloads."

def cleanup_temp():
    temp_dir = os.environ.get("TEMP")
    deleted = 0
    if os.path.exists(temp_dir):
        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                    deleted += 1
                except:
                    pass
    return f"🧹 Cleaned {deleted} temp files."

def auto_cleanup():
    msg1 = cleanup_downloads()
    msg2 = cleanup_temp()
    return f"{msg1}\n{msg2}"
