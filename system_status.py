import psutil
import speedtest
import platform

def get_cpu_usage():
    return f"CPU is at {psutil.cpu_percent()} percent."

def get_ram_usage():
    ram = psutil.virtual_memory()
    used = ram.used // (1024 ** 3)
    total = ram.total // (1024 ** 3)
    return f"RAM usage is {used} GB out of {total} GB."

def get_disk_usage():
    disk = psutil.disk_usage('/')
    free = disk.free // (1024 ** 3)
    total = disk.total // (1024 ** 3)
    return f"Disk space: {free} GB free out of {total} GB."

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        status = "plugged in" if battery.power_plugged else "not charging"
        return f"Battery is at {battery.percent}% and is {status}."
    else:
        return "Battery status not available."

def get_network_speed():
    try:
        st = speedtest.Speedtest()
        download = round(st.download() / 1_000_000, 2)
        upload = round(st.upload() / 1_000_000, 2)
        return f"Download speed is {download} Mbps. Upload speed is {upload} Mbps."
    except:
        return "Could not test network speed."

def get_system_info(query):
    query = query.lower()
    if "cpu" in query:
        return get_cpu_usage()
    elif "ram" in query or "memory" in query:
        return get_ram_usage()
    elif "disk" in query or "storage" in query:
        return get_disk_usage()
    elif "battery" in query:
        return get_battery_status()
    elif "network" in query or "internet" in query:
        return get_network_speed()
    else:
        return "Sorry, I don't understand what system info you want."
