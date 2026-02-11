import json
import os
from datetime import datetime

class EchoEngine:
    """
    EZ-OS Layer: Echo Engine (Inteligência por Ressonância)
    Calcula a 'Sincronia' e 'Entropia' baseada no ritmo do usuário.
    """
    def __init__(self, memory_path='layer/data/memory_graph.json'):
        self.memory_path = memory_path

    def _get_events(self):
        if not os.path.exists(self.memory_path):
            return []
        with open(self.memory_path, 'r') as f:
            data = json.load(f)
            return [n for n in data.get("nodes", []) if n.get("label") == "event"]

    def calculate_resonance(self):
        events = self._get_events()
        if len(events) < 2:
            return {"sync": 1.0, "entropy": 0.0, "state": "HARMONY"}

        # Extrai intervalos entre eventos (em horas)
        timestamps = [datetime.fromisoformat(e["timestamp"]) for e in events]
        timestamps.sort()
        intervals = [(timestamps[i] - timestamps[i-1]).total_seconds() / 3600 for i in range(1, len(timestamps))]

        # Cálculo de Variância (Entropia de Ritmo)
        avg_interval = sum(intervals) / len(intervals)
        variance = sum((i - avg_interval) ** 2 for i in intervals) / len(intervals)
        
        # Sincronia: 1.0 (Ritmo Perfeito) -> 0.0 (Caos Total)
        sync = max(0.0, 1.0 - (variance / (avg_interval + 1)**2))
        
        # Determina o Estado de Ressonância
        if sync > 0.8:
            state = "RESONANCE" # Sincronia alta: Mascote em paz
        elif sync > 0.4:
            state = "DISSonance" # Ritmo irregular: Mascote inquieto
        else:
            state = "CHAOS" # Sem padrão: Mascote confuso

        return {
            "sync": round(sync, 2),
            "entropy": round(variance, 2),
            "state": state,
            "avg_cycle_hours": round(avg_interval, 1)
        }

if __name__ == "__main__":
    # Teste rápido
    engine = EchoEngine()
    print(engine.calculate_resonance())
