import json
import os
from datetime import datetime
import uuid

class MemoryGraph:
    def __init__(self, data_path='data/memory_graph.json'):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), data_path)
        self.graph = self._load_graph()

    def _load_graph(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                return json.load(f)
        return {
            "metadata": {"version": "1.0", "created_at": str(datetime.now())},
            "nodes": [],
            "edges": []
        }

    def save(self):
        with open(self.data_path, 'w') as f:
            json.dump(self.graph, f, indent=4)

    def add_node(self, label, properties):
        node = {
            "id": str(uuid.uuid4()),
            "label": label,
            "properties": properties,
            "timestamp": str(datetime.now())
        }
        self.graph["nodes"].append(node)
        return node["id"]

    def add_edge(self, source_id, target_id, relation):
        edge = {
            "source": source_id,
            "target": target_id,
            "relation": relation,
            "timestamp": str(datetime.now())
        }
        self.graph["edges"].append(edge)

    def get_nodes_by_label(self, label):
        return [n for n in self.graph["nodes"] if n["label"] == label]

    def get_latest_events(self, limit=10):
        events = self.get_nodes_by_label("event")
        return sorted(events, key=lambda x: x["timestamp"], reverse=True)[:limit]

    def get_game_by_id(self, game_id):
        games = [n for n in self.graph["nodes"] if n["label"] == "game" and n["id"] == game_id]
        return games[0] if games else None
