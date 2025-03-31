from Character import Character

# Clase que representa a los enemigos
class Opponent(Character):
    def __init__(self, x, y, health, is_star=False):
        super().__init__(x, y, health)
        self.is_star = is_star  # Atributo que indica si ha sido convertido en estrella

    def move(self):
        # Lógica para mover al enemigo
        pass

    def shoot(self):
        # Lógica para disparar
        pass

    def act(self):
        # Lógica para el comportamiento del enemigo
        pass
