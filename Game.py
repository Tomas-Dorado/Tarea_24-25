# Clase principal que representa el juego en su totalidad
class Game:
    def __init__(self):
        self.score = 0
        self.player = None
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
        print("Game ended!")