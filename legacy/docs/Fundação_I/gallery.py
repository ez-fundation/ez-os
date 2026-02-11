import os
import sys
from datetime import datetime

# Adiciona o diretório atual ao path para importações
sys.path.append(os.path.dirname(__file__))
from indexer import GameIndexer
from memory import MemoryGraph

class EZGallery:
    def __init__(self, games_dir='games'):
        self.root_dir = os.path.dirname(os.path.dirname(__file__))
        self.games_dir = os.path.join(self.root_dir, games_dir)
        self.indexer = GameIndexer()
        self.memory = MemoryGraph()

    def scan_games(self):
        """Escaneia o diretório de jogos e retorna uma lista de jogos integrados com a memória."""
        catalog = []
        if not os.path.exists(self.games_dir):
            return catalog

        for filename in os.listdir(self.games_dir):
            if filename.startswith('.') or os.path.isdir(os.path.join(self.games_dir, filename)):
                continue
            
            file_path = os.path.join(self.games_dir, filename)
            # 1. Identificação técnica (Hash/Indexer)
            game_info = self.indexer.identify_game(file_path)
            
            # 2. Busca de memórias no Grafo
            game_node = self._find_game_in_memory(game_info.get('hash'))
            memories = self._get_game_memories(game_node['id'] if game_node else None)
            
            catalog.append({
                "file_path": file_path,
                "filename": filename,
                "technical": game_info,
                "memory_node": game_node,
                "stats": {
                    "session_count": len([e for e in memories if e['properties'].get('type') == 'START']),
                    "last_played": memories[0]['timestamp'] if memories else "Nunca",
                    "resonance": self._calculate_resonance(memories)
                }
            })
        
        # Ordenar por ressonância (mais 'vivos' primeiro)
        return sorted(catalog, key=lambda x: x['stats']['resonance'], reverse=True)

    def _find_game_in_memory(self, game_hash):
        if not game_hash: return None
        games = self.memory.get_nodes_by_label("game")
        for g in games:
            if g['properties'].get('hash') == game_hash:
                return g
        return None

    def _get_game_memories(self, game_id):
        if not game_id: return []
        events = self.memory.get_nodes_by_label("event")
        return [e for e in events if e['properties'].get('game_id') == game_id]

    def _calculate_resonance(self, memories):
        """Calcula um valor de 'vida' para o jogo baseado na frequência e recência."""
        if not memories: return 0
        # Simplificado: count de sessões + bônus por ser recente
        return len(memories) 
