import sys
import os
import time
import subprocess

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'system'))
from memory import MemoryGraph
from indexer import GameIndexer

def launch_game(game_name, rom_path):
    memory = MemoryGraph()
    indexer = GameIndexer()

    # 1. Indexar o jogo e adicionar ao grafo se não existir
    game_node_properties = indexer.create_game_node(rom_path)
    game_id = memory.add_node(game_node_properties["label"], game_node_properties["properties"])
    memory.save()

    # 2. Registrar início
    print(f"Iniciando {game_name}...")
    start_id = memory.add_node("event", {
        "type": "START",
        "game_id": game_id,
        "description": f"Começou a jogar {game_name}"
    })
    memory.save()
    
    # 2. Simular execução (no R35S seria a chamada ao RetroArch)
    # subprocess.run(["retroarch", "-L", core_path, rom_path])
    print("Simulando jogo por 3 segundos...")
    time.sleep(3)
    
    # 3. Registrar fim
    print(f"Saindo de {game_name}.")
    stop_id = memory.add_node("event", {
        "type": "STOP",
        "game_id": game_id,
        "description": f"Parou de jogar {game_name}"
    })
    memory.add_edge(start_id, stop_id, "SESSION_END")
    memory.save()
    
    print("Memória registrada com sucesso.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        launch_game(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        launch_game(sys.argv[1], "games/mock_game.snes")
    else:
        launch_game("Tetris", "games/tetris.gb")
