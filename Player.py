from Character import Character

# Clase que representa al jugador principal
class Player(Character):
    def __init__(self, x, y, health, score=0):
        super().__init__(x, y, health)
        self.score = score

    def increase_score(self, points):
        self.score += points