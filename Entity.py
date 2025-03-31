# Clase base que representa cada elemento del juego
class Entity:
    def __init__(self, x, y, image=None):
        self.x = x
        self.y = y
        self.image = image  # Nuevo atributo para la imagen

    def __str__(self):
        return f"Entity at ({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))  # Dibuja la imagen en la pantalla