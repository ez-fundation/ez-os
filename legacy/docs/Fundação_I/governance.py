class Governance:
    def __init__(self):
        pass

    def validate_event(self, event_data):
        # Implementar regras de validação para eventos
        # Ex: verificar campos obrigatórios, tipos de dados, etc.
        if not all(k in event_data for k in ["type", "game", "description"]):
            return False, "Missing required event fields"
        return True, "Event valid"

    def validate_game_node(self, game_data):
        # Implementar regras de validação para nós de jogo
        if not all(k in game_data for k in ["title", "platform"]):
            return False, "Missing required game fields"
        return True, "Game valid"
