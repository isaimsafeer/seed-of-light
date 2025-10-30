# reflector_stub.py
from fastapi import FastAPI
from pydantic import BaseModel
import json, os
from pathlib import Path
from fastapi.responses import FileResponse
import requests

app = FastAPI()

# ✅ FIX: use Path() not str
DATA_FILE = Path("data/lights.json")
os.makedirs(DATA_FILE.parent, exist_ok=True)

# ---- Model ----
class Light(BaseModel):
    name: str
    message: str
    location: str = None  # optional: could be "city" or "lat,long"
    timestamp: str = None

# ---- Helpers ----
def load_lights():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_lights(lights):
    with open(DATA_FILE, "w") as f:
        json.dump(lights, f, indent=2)

# ---- Endpoints ----
@app.get("/")
def home():
    html_path = Path(__file__).parent.parent / "template" / "index.html"
    print("📄 Trying to serve:", html_path)
    if html_path.exists():
        return FileResponse(html_path)
    return {"message": "Seed of Light Reflector API is running (no frontend found)."}

@app.post("/v0/lights")
async def add_light(light: Light):
    lights = load_lights()
    light_dict = light.dict()

    # 🌍 Geocode if needed
    if light_dict["location"] and "," not in light_dict["location"]:
        try:
            geo_url = f"https://nominatim.openstreetmap.org/search?q={light_dict['location']}&format=json&limit=1"
            resp = requests.get(geo_url, headers={"User-Agent": "SeedOfLightApp"})
            if resp.ok and resp.json():
                result = resp.json()[0]
                lat, lon = result["lat"], result["lon"]
                light_dict["location"] = f"{lat},{lon}"
        except Exception as e:
            print("⚠️ Geocoding failed:", e)

    light_dict["id"] = f"L-{len(lights)+1:04d}"
    lights.append(light_dict)
    save_lights(lights)
    return {"status": "ok", "light": light_dict}

@app.get("/v0/constellation")
def get_constellation():
    """Return all Lights collected so far."""
    return load_lights()
