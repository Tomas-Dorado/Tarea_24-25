from Opponent import Opponent

class Boss(Opponent):
    def __init__(self, x, y, base_speed, health):
        super().__init__(x, y, base_speed)
        self.health = health

    def __str__(self):
        return f"Boss at ({self.x}, {self.y}), Speed: {self.speed}, Health: {self.health}"

    def move(self):
        print(f"Boss moves at speed {self.speed}")

    def take_damage(self, damage):
        self.health -= damage
        print(f"Boss takes {damage} damage, remaining health: {self.health}")