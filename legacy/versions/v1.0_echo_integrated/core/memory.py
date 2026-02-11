import json
import os
from datetime import datetime
import uuid

class MemoryGraph:
    """
    EZ-OS Core: Memory Graph (Fonte de Verdade Factual)
    Regra: Append-only, Factual, Sem inferência.
    """
    def __init__(self, data_path='layer/data/memory_graph.json'):
        # No contexto do Core, o caminho é relativo à raiz do sistema instalado
        self.data_path = data_path
        self.graph = self._load_graph()

    def _load_graph(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                return json.load(f)
        return {
            "metadata": {"version": "1.0-FINAL", "created_at": str(datetime.now())},
            "nodes": [],
            "edges": []
        }

    def save(self):
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        with open(self.data_path, 'w') as f:
            json.dump(self.graph, f, indent=4)

    def add_event(self, event_type, properties):
        """Adiciona evento factual ao grafo (Append-only)"""
        node = {
            "id": str(uuid.uuid4()),
            "label": "event",
            "type": event_type, # START, STOP
            "properties": properties,
            "timestamp": str(datetime.now())
        }
        self.graph["nodes"].append(node)
        self.save()
        return node["id"]

    def get_nodes_by_label(self, label):
        return [n for n in self.graph["nodes"] if n.get("label") == label]

    def get_latest_events(self, limit=10):
        events = self.get_nodes_by_label("event")
        return sorted(events, key=lambda x: x["timestamp"], reverse=True)[:limit]
