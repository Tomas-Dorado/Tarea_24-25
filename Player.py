from Character import Character
import time

# Clase que representa al jugador principal
class Player(Character):
    def __init__(self, x, y, health, score=0, lives=3):
        super().__init__(x, y, health)
        self.score = score
        self.lives = lives

    def __str__(self):
        return f"Player at ({self.x}, {self.y}), Health: {self.health}, Score: {self.score}, Lives: {self.lives}, Is Alive: {self.is_alive}"
    
    def increase_score(self, points):
        self.score += points

    def move(self, dx, dy):
        # Actualiza la posición del jugador
        self.x += dx
        self.y += dy

    def shoot(self):
        # Lógica para disparar (puedes personalizarla según tu juego)
        print("Player is shooting!")

    def take_damage(self, damage):
        # Resta salud al jugador
        self.health -= damage
        if self.health <= 0:
            self.lives -= 1
            if self.lives > 0:
                print("Player lost a life! Respawning...")
                self.respawn()
            else:
                print("Game Over!")
                self.is_alive = False

    def respawn(self):
        # Lógica para renacer al jugador
        time.sleep(2)  # Simula un breve tiempo de espera antes de renacer
        self.health = 100  # Restaura la salud del jugador
        self.x, self.y = 0, 0  # Reinicia la posición del jugador
        self.is_alive = True