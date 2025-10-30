# 🌱 Seeds of Light — AI Kindness Tracker

**Seeds of Light** is a simple open-source app that lets you log and visualize “acts of kindness” (called *Seeds* or *Lights*).  
Each act is stored locally (or in Railway’s ephemeral storage when deployed) and can later be synced with a global kindness map via a `LoveNode`.

---

## ✨ Features

- 📜 Log new acts of kindness (Seeds)
- 🗂️ Store entries in a local JSON file (`data/seeds.json`)
- 📊 View all seeds through API endpoints
- 🪴 Vote or add updates to existing seeds
- 🌍 (Optional) Connect with other kindness nodes using `lovenode.py`
- ⚡ FastAPI-powered backend, deployable to **Railway** in minutes

---

## 🧩 Project Structure

```
seeds-of-light/
│
├── scripts/
│   └── seeds_api_stub.py       # FastAPI backend with all API routes
│   └──   lovenode.py           # (Optional) Node sync helper
│
├── data/
│   └── seeds.json              # Local database for kindness entries
│
├── templates/
│   └── index.html              # frontend code  
├── requirements.txt            # Python dependencies
└── README.md                   # You are here!
```

---

## 🚀 Getting Started (Local Development)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/seeds-of-light.git
cd seeds-of-light
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the API locally
```bash
cd api
uvicorn seeds_api_stub:app --reload
```

Your app will now be running at:
```
http://127.0.0.1:8000
```

---

## ⚙️ Railway Deployment

### ✅ Build Command
```bash
pip install -r requirements.txt
```

### ✅ Start Command
```bash
uvicorn api.seeds_api_stub:app --host 0.0.0.0 --port ${PORT}
```

Or just use this **Procfile**:
```
web: uvicorn api.seeds_api_stub:app --host 0.0.0.0 --port ${PORT}
```

After deployment, Railway will give you a public URL like:
```
https://kind-rejoicing.up.railway.app
```

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| **GET** | `/v0/seeds` | Fetch all logged seeds |
| **POST** | `/v0/seeds` | Add a new seed (act of kindness) |
| **POST** | `/v0/update/{seed_id}` | Add an update/note to a specific seed |
| **POST** | `/v0/vote/{seed_id}` | Vote or support a specific seed |

### Example Request
```bash
POST /v0/seeds
Content-Type: application/json

{
  "title": "Helped a neighbor carry groceries",
  "description": "Saw them struggling and offered help",
  "tags": ["community", "kindness"]
}
```

---

## 🌍 LoveNode (Optional)

`lovenode.py` acts as a local “bridge” or **node** that can sync your kindness data to a global map or network.  
Its goal is to let individual kindness logs (Seeds) from different people connect to a shared “Seeds of Light” ecosystem.

You can run it separately to experiment with peer-to-peer kindness sharing.

---

## 🧠 Tech Stack

- **FastAPI** — lightweight, modern web framework for APIs  
- **Uvicorn** — blazing-fast ASGI server  
- **Pydantic** — robust data validation  
- **Railway** — simple, free cloud deployment

---

## 📖 API Docs

Once the app is running, you can access:
- Swagger UI → [`/docs`](http://127.0.0.1:8000/docs)
- ReDoc → [`/redoc`](http://127.0.0.1:8000/redoc)

Example (on Railway):  
`https://kind-rejoicing.up.railway.app/docs`

---

## 🧩 Future Enhancements
- 🌐 Real-time sync between local and global Seeds
- 🪄 Frontend Flutter app for mobile users
- 🔒 Authentication and moderation tools
- 💌 AI summaries of community kindness data

---

## 🩵 Author
**Seeds of Light Project**  
Open-source community project to spread kindness through technology.  
Made with ☀️, FastAPI, and love.

---

## 📜 License
This project is open-source under the **MIT License** — free to use, modify, and share.
