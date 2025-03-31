from Character import Character

# Clase que representa a los enemigos
class Opponent(Character):
    def __init__(self, x, y, health, is_star=False):
        super().__init__(x, y, health)
        self.is_star = is_star  # Atributo que indica si ha sido convertido en estrella
    
    def __str__(self):
        return f"Opponent at ({self.x}, {self.y}), Health: {self.health}, Is Star: {self.is_star}, Is Alive: {self.is_alive}"

    def move(self):
        # Lógica para mover al enemigo
        pass

    def shoot(self):
        # Lógica para disparar
        pass

    def act(self):
        # Lógica para el comportamiento del enemigo
        pass
