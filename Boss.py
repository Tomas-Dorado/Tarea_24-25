from Opponent import Opponent


class FinalBoss(Opponent):
    def __init__(self,x,y, base_speed):
        super().__init__(x,y,base_speed * 2)

    def __str__(self):
        return f"Final Boss at ({self.x}, {self.y}), Speed: {self.speed}"
    
    def move(self):
        print(f"Final Boss moves at speed {self.speed}")


# Example usage
def on_enemy_defeated():
    print("Enemy defeated! Final Boss appears!")
    final_boss = FinalBoss(base_speed=5)
    final_boss.move()


# Simulate defeating an enemy
on_enemy_defeated()