from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from datetime import datetime
import sys
import os

# Adiciona o diretório system ao path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'system'))
from memory import MemoryGraph
from companion import Companion
from gallery import EZGallery
from symbiosis import EZSymbiosis

class EZOS_TUI:
    def __init__(self):
        self.console = Console()
        self.memory = MemoryGraph()
        self.gallery = EZGallery()
        self.symbiosis = EZSymbiosis()
        self.companion = Companion(seed="user-123") # Mock seed
        self.companion.update_state(self.memory)
        self.insights = self.symbiosis.generate_insights(self.memory)

    def make_layout(self) -> Layout:
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3)
        )
        layout["main"].split_row(
            Layout(name="side", size=30),
            Layout(name="body", ratio=1)
        )
        return layout

    def get_header(self):
        return Panel(
            Text("EZ-OS | Sistema Operacional de Memória Lúdica", justify="center", style="bold cyan"),
            style="white"
        )

    def get_sidebar(self, active_menu="Galeria"):
        stats = self.companion.state
        content = f"[bold cyan]Mascote:[/bold cyan] {self.companion.name}\n"
        content += f"[bold cyan]Fase:[/bold cyan] {stats['phase']}\n"
        content += f"[bold cyan]Energia:[/bold cyan] [green]{stats['energy']}%[/green]\n"
        content += f"[bold cyan]Foco:[/bold cyan] {stats['focus']}\n\n"
        content += "[dim]────────────────────[/dim]\n\n"
        content += "[bold yellow]MENU[/bold yellow]\n"
        
        menus = ["Galeria", "Memórias"]
        # Adiciona opções adaptativas da simbiose
        adaptive_options = self.symbiosis.get_adaptive_menu_options()
        menus.extend(adaptive_options)
        menus.extend(["Config", "Sair"])

        for m in menus:
            if m == active_menu:
                content += f"▶ [bold reverse white]{m}[/bold reverse white]\n"
            else:
                content += f"  [white]{m}[/white]\n"
        
        return Panel(content, title="[bold blue]Status[/bold blue]", border_style="blue")

    def get_gallery_view(self):
        catalog = self.gallery.scan_games()
        
        table = Table(expand=True, border_style="dim", box=None)
        table.add_column("Ressonância", justify="center", style="bold magenta")
        table.add_column("Título", style="bold white")
        table.add_column("Plataforma", style="cyan")
        table.add_column("Última Sessão", style="dim")
        
        for item in catalog:
            res_icon = "★" * min(item['stats']['resonance'], 3) if item['stats']['resonance'] > 0 else "○"
            table.add_row(
                res_icon,
                item['technical']['title'],
                item['technical'].get('platform', '---'),
                item['stats']['last_played'][:16]
            )

        return Panel(table, title="[bold yellow]EZ-Gallery | Catálogo de Memória[/bold yellow]", border_style="yellow")

    def get_body(self, view_mode="gallery"):
        ascii_art = self.companion.get_ascii_art()
        
        # Área de Insights do Mascote (Simbiose)
        insight_panel = None
        if self.insights:
            insight = self.insights[0] # Pega o primeiro insight para exibição
            insight_panel = Panel(
                Text(f"💡 {insight['message']}", style="italic yellow"),
                title=f"[bold cyan]Insight: {insight['target']}[/bold cyan]",
                border_style="cyan"
            )

        body_content = Layout()
        
        if view_mode == "gallery":
            main_view = Layout()
            if insight_panel:
                main_view.split_column(
                    Layout(insight_panel, size=5),
                    Layout(self.get_gallery_view(), ratio=1)
                )
            else:
                main_view.update(self.get_gallery_view())

            body_content.split_column(
                Layout(Panel(Text(ascii_art, justify="center", style="bold yellow"), title="[bold green]Companion[/bold green]", border_style="green"), size=12),
                main_view
            )
        else:
            events = self.memory.get_latest_events(5)
            table = Table(expand=True, border_style="dim")
            table.add_column("Data", style="dim", width=20)
            table.add_column("Evento", style="white")
            for e in events:
                table.add_row(e["timestamp"][:16], e["properties"].get("description", "Evento desconhecido"))
            
            body_content.split_column(
                Layout(Panel(Text(ascii_art, justify="center", style="bold yellow"), title="[bold green]Companion[/bold green]", border_style="green"), ratio=2),
                Layout(Panel(table, title="[bold magenta]Log de Memória[/bold magenta]", border_style="magenta"), ratio=1)
            )
        
        return body_content

    def run(self):
        layout = self.make_layout()
        layout["header"].update(self.get_header())
        layout["side"].update(self.get_sidebar())
        layout["body"].update(self.get_body())
        layout["footer"].update(Panel(Text("O EZ-OS não tenta prender o jogador. Ele apenas lembra quando ele volta.", justify="center", style="italic dim")))
        
        self.console.print(layout)

if __name__ == "__main__":
    tui = EZOS_TUI()
    tui.run()
