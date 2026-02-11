import time
import os
import random
from core.memory import MemoryGraph
from core.companion import Companion
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.live import Live

class EZOSVirtualPet:
    def __init__(self):
        # Garante que o diretório de dados existe
        os.makedirs('layer/data', exist_ok=True)
        self.memory = MemoryGraph(data_path='layer/data/memory_graph.json')
        self.companion = Companion(seed="user-soul-01")
        self.console = Console()

    def make_layout(self):
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=3)
        )
        return layout

    def update_display(self, layout):
        self.companion.update_state(self.memory)
        
        # Header
        layout["header"].update(Panel(Text(f"EZ-OS v1.0 | IDENTIDADE: {self.companion.name}", justify="center", style="bold cyan")))
        
        # Body (Mascote + Status)
        ascii_art = self.companion.get_ascii_art()
        events_count = len(self.memory.get_nodes_by_label("event"))
        
        status_text = Text()
        status_text.append(f"\n{ascii_art}\n", style="bold green")
        status_text.append(f"\nFASE: {self.companion.state['phase']}", style="yellow")
        status_text.append(f" | MODO: {self.companion.state['modifier']}\n", style="magenta")
        status_text.append(f"EVENTOS REGISTRADOS: {events_count}", style="dim")
        
        layout["body"].update(Panel(status_text, title="[Simbiose Ativa]", border_style="green"))
        
        # Footer
        layout["footer"].update(Panel(Text("Pressione Ctrl+C para encerrar o ciclo.", justify="center", style="italic dim")))

    def run_simulation(self):
        layout = self.make_layout()
        with Live(layout, refresh_per_second=2, screen=True) as live:
            try:
                while True:
                    # Simula um evento aleatório a cada 5 segundos para demonstração
                    if random.random() < 0.1:
                        self.memory.add_event("START", {"game": "Simulation_Tick", "source": "Virtual_Pet_Demo"})
                    
                    self.update_display(layout)
                    time.sleep(0.5)
            except KeyboardInterrupt:
                self.console.print("\n[bold red]Ciclo de simbiose interrompido.[/bold red]")

if __name__ == "__main__":
    pet = EZOSVirtualPet()
    pet.run_simulation()
