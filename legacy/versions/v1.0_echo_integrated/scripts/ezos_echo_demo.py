import time
import os
from layer.echo_engine import EchoEngine
from core.memory import MemoryGraph
from core.companion import Companion
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.live import Live

class EZOSEchoDemo:
    def __init__(self):
        self.engine = EchoEngine(memory_path='ez-os-final/layer/data/memory_graph.json')
        self.memory = MemoryGraph(data_path='ez-os-final/layer/data/memory_graph.json')
        self.companion = Companion(seed="user-soul-01")
        self.console = Console()

    def make_layout(self):
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="echo", size=6),
            Layout(name="footer", size=3)
        )
        return layout

    def update_display(self, layout):
        self.companion.update_state(self.memory)
        res = self.engine.calculate_resonance()
        
        # Header
        layout["header"].update(Panel(Text(f"EZ-OS v1.0 | RITMO: {res['state']}", justify="center", style="bold cyan")))
        
        # Body (Companion)
        ascii_art = self.companion.get_ascii_art()
        layout["body"].update(Panel(Text(f"\n{ascii_art}\n", justify="center", style="green"), title="Companion State"))
        
        # Echo Data (The Intelligence)
        echo_text = Text()
        echo_text.append(f"SINCRONIA: {res['sync']*100}% ", style="bold yellow")
        echo_text.append(f"| ENTROPIA: {res['entropy']}\n", style="magenta")
        echo_text.append(f"CICLO MÉDIO: {res['avg_cycle_hours']} horas\n", style="cyan")
        
        bar = "█" * int(res['sync'] * 20) + "░" * (20 - int(res['sync'] * 20))
        echo_text.append(f"RESSONÂNCIA: [{bar}]", style="bold green")
        
        layout["echo"].update(Panel(echo_text, title="Módulo Echo (Ressonância Temporal)"))
        
        # Footer
        layout["footer"].update(Panel(Text("O sistema agora sente o seu ritmo.", justify="center", style="italic dim")))

    def run(self):
        layout = self.make_layout()
        with Live(layout, refresh_per_second=2, screen=True) as live:
            try:
                while True:
                    self.update_display(layout)
                    time.sleep(1)
            except KeyboardInterrupt:
                pass

if __name__ == "__main__":
    EZOSEchoDemo().run()
