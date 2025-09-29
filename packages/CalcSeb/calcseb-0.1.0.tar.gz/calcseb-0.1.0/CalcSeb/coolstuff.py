import random

class FrasesDesarrollador:
    """Clase que contiene frases típicas de desarrolladores."""

    def __init__(self):
        self.frases = [
            "Hola Julian . Sebastian Rodriguez Garcia",
            "Tau mejor que pi. Julian Avila"
        ]

    def mostrar_frase(self):
        """Devuelve una frase aleatoria."""
        return random.choice(self.frases)