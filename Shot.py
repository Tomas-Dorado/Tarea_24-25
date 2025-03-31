from Entity import Entity

# Clase que representa los disparos realizados por un personaje
class Shot(Entity):
    def __init__(self, x, y, speed, direction):
        super().__init__(x, y)
        self.speed = speed
        self.direction = direction

    def update_position(self):
        self.move(self.speed * self.direction[0], self.speed * self.direction[1])