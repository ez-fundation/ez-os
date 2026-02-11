class Governance:
    """
    EZ-OS Core: Governança (Inalterável)
    Regra: Validar limites e impedir funções externas no Core.
    """
    @staticmethod
    def validate_event(event_type):
        return event_type in ["START", "STOP"]

    @staticmethod
    def get_constraints():
        return {
            "offline_only": True,
            "no_telemetry": True,
            "no_auto_update": True,
            "append_only_memory": True
        }
