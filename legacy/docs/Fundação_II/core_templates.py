# Template: Core Memory Graph (Append-Only)
import json, os, uuid
from datetime import datetime

class MemoryGraph:
    def __init__(self, path):
        self.path = path
        self.data = self._load()
    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f: return json.load(f)
        return {"nodes": [], "edges": []}
    def add_event(self, type, props):
        event = {"id": str(uuid.uuid4()), "type": type, "props": props, "ts": str(datetime.now())}
        self.data["nodes"].append(event)
        with open(self.path, 'w') as f: json.dump(self.data, f)

# Template: Deterministic Companion
import hashlib, random

class Companion:
    def __init__(self, seed):
        self.seed = seed
    def get_state(self, events):
        h = int(hashlib.md5(self.seed.encode()).hexdigest(), 16)
        random.seed(h)
        # Lógica baseada no volume de eventos
        count = len(events)
        return "Phase: " + ("New" if count < 10 else "Elder")
