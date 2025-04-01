from Boss import Boss
from Player import Player
from Opponent import Opponent
# Clase principal que representa el juego en su totalidad
class Game:
    def __init__(self):
        self.score = 0
        self.player = Player()
        self.opponents = []
        self.shots = []
        self.is_running = False

    def add_player(self, player):
        self.player = player

    def add_opponent(self, opponent):
        self.opponents.append(opponent)

    def add_shot(self, shot):
        self.shots.append(shot)

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if not self.is_running:
            return

        # Actualizar posiciones de disparos
        for shot in self.shots:
            shot.update_position()

        # Lógica adicional para actualizar el estado del juego
        pass

    def end_game(self):
        self.is_running = False
        if self.player and self.player.lives > 0 and all(isinstance(opponent, FinalBoss) for opponent in self.opponents):
            print("Victory! You defeated the Final Boss!")
        else:
            print("Game ended!")

    def convert_opponent_to_star(self, opponent):
        if opponent in self.opponents:
            self.opponents.remove(opponent)
            print(f"Opponent {opponent} converted to a star!")
            
    def increment_score(self, points):
        self.score += points
        print(f"Score updated: {self.score}")

    def check_player_hit(self, enemy_shot):
        if self.player and self.player.is_hit_by(enemy_shot):
            self.player.lives -= 1
            print(f"Player hit! Lives remaining: {self.player.lives}")
            if self.player.lives <= 0:
                self.end_game()

    def spawn_final_boss(self):
        if len(self.opponents) == 0 and self.is_running:
            final_boss = Boss(speed=2 * Opponent.speed)
            self.add_opponent(final_boss)
            print("Final Boss has appeared!")

    def reset_score(self):
        self.score = 0
        print("Score reset to 0.")

    def display_score_and_lives(self):
        if not self.is_running:
            print("Game is not running.")
        elif self.player:
            print(f"Score: {self.score} | Lives: {self.player.lives}")

    def remove_opponent(self, opponent):
        if opponent in self.opponents:
            self.opponents.remove(opponent)
            print(f"Opponent {opponent} removed!")
            if len(self.opponents) == 0:
                self.spawn_final_boss()