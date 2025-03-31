from Entity import Entity

# Clase que representa los disparos realizados por un personaje
class Shot(Entity):
    def __init__(self, x, y, speed, direction):
        super().__init__(x, y)
        self.speed = speed
        self.direction = direction

    def __str__(self):
        return f"Shot at ({self.x}, {self.y}), Speed: {self.speed}, Direction: {self.direction}"
    
    def move(self, dx, dy):
        """Actualiza la posición del disparo."""
        self.x += dx
        self.y += dy

    def hit_target(self, target):
        """Verifica si el disparo ha alcanzado un objetivo."""
        return self.x == target.x and self.y == target.y

    def update_position(self):
        self.move(self.speed * self.direction[0], self.speed * self.direction[1])