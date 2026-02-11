import hashlib
import random

class Companion:
    """
    EZ-OS Core: Companion (Mascote Lógico)
    Regra: Procedural determinístico, Renderizador de estado silencioso.
    """
    def __init__(self, seed="ez-os-default"):
        self.seed = seed
        self.name = self._generate_name()
        self.state = {
            "phase": "Ovo",
            "modifier": "Observer"
        }

    def _generate_name(self):
        prefixes = ["Neo", "Zel", "Pix", "Bit", "Aura", "Giga", "Moni"]
        suffixes = ["mon", "bot", "tron", "core", "link", "oid"]
        h = int(hashlib.md5(self.seed.encode()).hexdigest(), 16)
        random.seed(h)
        return random.choice(prefixes) + random.choice(suffixes)

    def get_ascii_art(self):
        if self.state["phase"] == "Ovo":
            return """
           .---.
          /     \\
         |  (O)  |
          \\     /
           '---'
            """
        elif self.state["phase"] == "Jovem":
            return """
             ^---^
            ( o o )
             \\ v /
            /     \\
            |     |
            """
        elif self.state["phase"] == "Adulto":
            return """
          (O)     (O)
           \\       /
        .---'-----'---.
       /   _       _   \\
    --|   (O)     (O)   |--
   /  |        -        |  \\
  {   \\      '---'      /   }
   \\   '---------------'   /
    '---'             '---'
            """
        else: # Sábio
            return """
             _______
          /|  _   _  |\\
         | | (O) (O) | |
         | |    V    | |
         |  \\  ---  /  |
          \\  '-----'  /
           '---------'
             /     \\
            """

    def update_state(self, memory_graph):
        events = memory_graph.get_nodes_by_label("event")
        count = len(events)
        
        if count == 0:
            self.state["phase"] = "Ovo"
        elif count < 10:
            self.state["phase"] = "Jovem"
        elif count < 50:
            self.state["phase"] = "Adulto"
        else:
            self.state["phase"] = "Sábio"

        self.state["modifier"] = "Archivist" if count > 0 else "Observer"
