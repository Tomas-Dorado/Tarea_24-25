from Character import Character
from Shot import Shot

# Clase que representa a los enemigos
class Opponent(Character):
    def __init__(self, x, y, health, is_star=False):
        super().__init__(x, y, health)
        self.is_star = is_star  # Atributo que indica si ha sido convertido en estrella
    
    def __str__(self):
        return f"Opponent at ({self.x}, {self.y}), Health: {self.health}, Is Star: {self.is_star}, Is Alive: {self.is_alive}"

    def move(self, direction="down"):
        # Lógica para mover al enemigo hacia arriba o hacia abajo
        if direction == "down":
            self.y += 1
        elif direction == "up":
            self.y -= 1

    def shoot(self):
        # Crea un disparo desde la posición actual del oponente
        return Shot(self.x, self.y + 1, "down")

    def act(self):
        # Lógica para el comportamiento del enemigo
        pass

    def collide(self, score):
        # Lógica para manejar la colisión con un disparo
        if self.is_alive:  # Solo suma puntos si el oponente está vivo
            self.health -= 1  # Reduce la salud del oponente
            if self.health <= 0:
                self.is_alive = False
                score += 1  # Suma un punto a la puntuación
        return score
