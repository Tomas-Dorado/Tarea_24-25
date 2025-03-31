from Entity import Entity

# Clase que representa cualquier personaje con vida dentro del juego
class Character(Entity):
    def __init__(self, x, y, health):
        super().__init__(x, y)
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0