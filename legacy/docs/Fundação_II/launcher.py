import sys
import os
from memory import MemoryGraph
from governance import Governance

def main():
    if len(sys.argv) < 3:
        print("Usage: launcher.py <START|STOP> <game_id>")
        sys.exit(1)

    action = sys.argv[1]
    game_id = sys.argv[2]

    if not Governance.validate_event(action):
        print(f"Invalid action: {action}")
        sys.exit(1)

    # Inicializa memória (caminho relativo à raiz da instalação)
    memory = MemoryGraph()
    memory.add_event(action, {"game": game_id, "source": "ArkOS_Hook"})
    
    print(f"EZ-OS: Event {action} registered for {game_id}")

if __name__ == "__main__":
    main()
