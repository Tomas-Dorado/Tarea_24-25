from Entity import Entity
from Shot import Shot  # Import the Shot class

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
        # Update the character's position based on the given direction
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        else:
            print("Invalid direction. Use 'up', 'down', 'left', or 'right'.")

    def shoot(self):
        # Create a new shot originating from the character's position
        shot = Shot(self.x, self.y, self.direction)
        print(f"Shot fired from ({self.x}, {self.y}) in direction '{self.direction}'")
        return shot

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

    