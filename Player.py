from Character import Character

# Clase que representa al jugador principal
class Player(Character):
    def __init__(self, x, y, health, score=0, lives=3):
        super().__init__(x, y, health)
        self.score = score
        self.lives = lives

    def increase_score(self, points):
        self.score += points

    def move(self, dx, dy):
        # Actualiza la posición del jugador
        self.x += dx
        self.y += dy

    def shoot(self):
        # Lógica para disparar (puedes personalizarla según tu juego)
        print("Player is shooting!")