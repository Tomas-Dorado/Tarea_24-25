from Character import Character

# Clase que representa a los enemigos
class Opponent(Character):
    def __init__(self, x, y, health, behavior):
        super().__init__(x, y, health)
        self.behavior = behavior

    def act(self):
        # Lógica para el comportamiento del enemigo
        pass
