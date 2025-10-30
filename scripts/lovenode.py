# lovenode.py
import json
import os
import requests
from datetime import datetime

DATA_FILE = 'lights.json'
REFLECTOR_URL = 'https://your-live-api-url.onrender.com/v0/lights'  # Replace with your deployed Reflector URL

os.makedirs(os.path.dirname(DATA_FILE) or '.', exist_ok=True)

def load_lights():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_lights(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_light(name, message, location=None):
    """Logs an act of kindness (a Light) locally and sends it to the reflector."""
    lights = load_lights()
    light = {
        "light_id": f"LIGHT-{len(lights)+1:04d}",
        "name": name,
        "message": message,
        "location": location,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    lights.append(light)
    save_lights(lights)

    print(f"✨ Logged Light: {light['message']}")

    # Try to send to Reflector
    try:
        res = requests.post(REFLECTOR_URL, json=light, timeout=5)
        if res.status_code == 200:
            print("✅ Sent to Reflector:", res.json())
        else:
            print(f"⚠️ Reflector returned status {res.status_code}")
    except Exception as e:
        print("⚠️ Could not send to Reflector:", e)

if __name__ == "__main__":
    # Example usage
    print("🌱 Welcome to the Seed of Light local logger.")
    name = input("Your name: ")
    message = input("What act of kindness did you do today? ")
    location = input("Where did it happen (optional): ") or None

    log_light(name, message, location)
