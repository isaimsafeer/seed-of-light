from fastapi import FastAPI
from pydantic import BaseModel
import json, os

app = FastAPI()
DATA_FILE = 'data/seeds.json'
os.makedirs('data', exist_ok=True)

class Seed(BaseModel):
    title: str
    description: str
    status: str = 'germinating'
    votes: int = 0
    updates: list = []
    tags: list = []

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.get('/v0/seeds')
def get_seeds():
    return load_data()

@app.post('/v0/seeds')
def add_seed(seed: Seed):
    data = load_data()
    seed_dict = seed.dict()
    seed_dict['seed_id'] = f'SOL-{len(data)+1:04d}'
    data.append(seed_dict)
    save_data(data)
    return {'status': 'ok', 'seed': seed_dict}

@app.post('/v0/update/{seed_id}')
def add_update(seed_id: str, update: dict):
    data = load_data()
    for seed in data:
        if seed['seed_id'] == seed_id:
            seed['updates'].append(update)
            save_data(data)
            return {'status': 'updated', 'seed': seed}
    return {'error': 'not found'}

@app.post('/v0/vote/{seed_id}')
def vote_seed(seed_id: str):
    data = load_data()
    for seed in data:
        if seed['seed_id'] == seed_id:
            seed['votes'] += 1
            save_data(data)
            return {'status': 'voted', 'votes': seed['votes']}
    return {'error': 'not found'}
