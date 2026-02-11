import os
import platform
import subprocess

class EZSymbiosis:
    def __init__(self):
        self.hardware_profile = self._detect_hardware()
        self.insights = []

    def _detect_hardware(self):
        """Mapeia as capacidades do dispositivo atual."""
        profile = {
            "os": platform.system(),
            "arch": platform.machine(),
            "cpu_cores": os.cpu_count(),
            "features": [],
            "hidden_resources": []
        }
        
        # Simulação de detecção de recursos específicos de consoles retro (R35S/Linux)
        # Em um dispositivo real, leríamos /proc/cpuinfo ou arquivos de sysfs
        if profile["os"] == "Linux":
            profile["features"].append("RetroArch Integration")
            profile["hidden_resources"].append({
                "name": "Overclock Seguro",
                "description": "Ajuste de CPU para jogos de PSP/N64",
                "status": "Subutilizado"
            })
            profile["hidden_resources"].append({
                "name": "Mapeamento L2/R2",
                "description": "Atalhos rápidos para Save State nos botões traseiros",
                "status": "Não configurado"
            })
            profile["hidden_resources"].append({
                "name": "Scripts de Limpeza de RAM",
                "description": "Liberação de memória antes de carregar ROMs pesadas",
                "status": "Inativo"
            })
            
        return profile

    def generate_insights(self, memory_graph):
        """Gera insights baseados na simbiose entre uso (memória) e hardware."""
        self.insights = []
        events = memory_graph.get_nodes_by_label("event")
        
        # Exemplo de Insight: Se o usuário joga muito, sugerir mapeamento de botões
        if len(events) > 5:
            self.insights.append({
                "type": "TUTORIAL",
                "target": "Mapeamento L2/R2",
                "message": "Notei que você joga com frequência. Sabia que pode usar os botões traseiros para salvar seu progresso instantaneamente?"
            })
            
        # Exemplo de Insight: Se o sistema detecta hardware Linux, sugerir otimização
        if self.hardware_profile["os"] == "Linux":
            self.insights.append({
                "type": "OPTIMIZATION",
                "target": "Overclock Seguro",
                "message": "Este dispositivo possui fôlego extra. Posso ajustar a CPU para melhorar a fluidez em jogos mais pesados."
            })
            
        return self.insights

    def get_adaptive_menu_options(self):
        """Retorna opções de menu que se adaptam ao hardware detectado."""
        options = []
        if self.hardware_profile["os"] == "Linux":
            options.append("Otimizar Hardware")
            options.append("Configurar Atalhos L2/R2")
        return options
