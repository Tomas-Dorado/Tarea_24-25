from Entity import Entity

# Clase que representa cualquier personaje con vida dentro del juego
class Character(Entity):
    def __init__(self, x, y, lives):
        super().__init__(x, y)
        self.lives = lives

    def __str__(self):
        return f"Character at ({self.x}, {self.y}), Health: {self.health}, Lives: {self.lives}, Is Alive: {self.is_alive}"

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False

    def move(self, direction):
       pass

    def shoot(self):
        pass

    def collide(self, other):
        # Check if the other object is an instance of Entity
        if isinstance(other, Entity):
            # Simple collision logic: check if positions overlap
            if self.x == other.x and self.y == other.y:
                print(f"Collision detected with {other}")
                self.take_damage(1)  # Example: take 1 damage on collision
        else:
            print("Collision with non-entity object ignored.")

    def reset(self):
        # Reset character's state
        self.lives = 3

    