from Entity import Entity

# Clase que representa cualquier personaje con vida dentro del juego
class Character(Entity):
    def __init__(self, x, y, health, lives):
        super().__init__(x, y)
        self.health = health
        self.lives = lives
        self.is_alive = True

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def shoot(self):
        # Implement shooting logic here
        print("Character is shooting!")

    def collide(self, other):
        # Implement collision logic here
        print(f"Character collided with {other}")