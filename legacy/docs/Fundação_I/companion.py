import random
import hashlib

class Companion:
    def __init__(self, seed="ez-os-default"):
        self.seed = seed
        self.name = self._generate_name()
        self.state = {
            "phase": "Ovo",
            "energy": 100,
            "focus": "Nenhum"
        }

    def _generate_name(self):
        prefixes = ["Neo", "Zel", "Pix", "Bit", "Aura", "Giga", "Moni"]
        suffixes = ["mon", "bot", "tron", "core", "link", "oid"]
        
        # Deterministic random based on seed
        h = int(hashlib.md5(self.seed.encode()).hexdigest(), 16)
        random.seed(h)
        
        return random.choice(prefixes) + random.choice(suffixes)

    def get_ascii_art(self):
        # Baseado na imagem enviada pelo usuário
        # Foco em: Antenas com esferas, olhos grandes, corpo arredondado, pequenas asas
        
        phase = self.state["phase"]
        
        if phase == "Ovo":
            return """
           .---.
          /     \\
         |  (O)  |
          \     /
           '---'
            """
        
        # Forma Canônica (Inspirada no "AS(I) ART" da imagem)
        return """
          (O)     (O)
           \       /
        .---'-----'---.
       /   _       _   \\
    --|   (O)     (O)   |--
   /  |        -        |  \\
  {   \      '---'      /   }
   \   '---------------'   /
    '---'             '---'
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
            
        # Lógica de energia baseada no tempo do último evento (mock por enquanto)
        self.state["energy"] = 100
