import hashlib
import json
import os

class GameIndexer:
    def __init__(self, metadata_db_path='data/metadata_cache.json'):
        self.metadata_db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), metadata_db_path)
        self.cache = self._load_cache()

    def _load_cache(self):
        if os.path.exists(self.metadata_db_path):
            with open(self.metadata_db_path, 'r') as f:
                return json.load(f)
        return {}

    def calculate_hash(self, file_path):
        """Calcula o hash SHA1 para identificação precisa (No-Intro/Redump style)"""
        if not os.path.exists(file_path):
            return None
        
        sha1 = hashlib.sha1()
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()

    def identify_game(self, file_path):
        """Simula a identificação de um jogo via hash contra bases canônicas"""
        file_hash = self.calculate_hash(file_path)
        if not file_hash:
            return {"title": os.path.basename(file_path), "status": "unknown"}
        
        # Mock de busca em base Libretro/No-Intro
        # Em uma implementação real, isso consultaria um arquivo .dat ou .json local
        return {
            "title": os.path.basename(file_path).split('.')[0],
            "hash": file_hash,
            "identified_via": "Local Hash Check",
            "platform": "Detected via Extension"
        }

    def create_game_node(self, file_path):
        info = self.identify_game(file_path)
        return {
            "label": "game",
            "properties": {
                "title": info["title"],
                "hash": info.get("hash"),
                "platform": info.get("platform", "Unknown"),
                "source": "User Provided",
                "indexed_at": "now"
            }
        }
