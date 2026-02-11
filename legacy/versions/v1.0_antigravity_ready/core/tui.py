from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from memory import MemoryGraph
from companion import Companion

class EZOS_TUI:
    def __init__(self):
        self.console = Console()
        self.memory = MemoryGraph()
        self.companion = Companion(seed="user-r35s")
        self.companion.update_state(self.memory)

    def run(self):
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=3)
        )
        
        layout["header"].update(Panel(Text("EZ-OS v1.0-FINAL", justify="center", style="bold cyan")))
        
        ascii_art = self.companion.get_ascii_art()
        status = f"Mascote: {self.companion.name} | Fase: {self.companion.state['phase']} | Modo: {self.companion.state['modifier']}"
        
        layout["body"].update(Panel(
            Text(f"{ascii_art}\n\n{status}", justify="center"),
            title="[bold green]Companion[/bold green]"
        ))
        
        layout["footer"].update(Panel(Text("O EZ-OS apenas lembra quando você volta.", justify="center", style="italic dim")))
        
        self.console.print(layout)

if __name__ == "__main__":
    EZOS_TUI().run()
