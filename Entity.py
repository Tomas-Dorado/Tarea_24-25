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
    
    def get_position(self):
        # Devuelve la posición de la entidad
        return self.x, self.y
    
    def get_image(self):
        # Devuelve la imagen de la entidad
        return self.image
    
    def set_image(self, image):
        # Establece la imagen de la entidad
        self.image = image
        
    def set_position(self, x, y):
        # Establece la posición de la entidad
        self.x = x
        self.y = y

    def collide(self, other):
        # Verifica si hay colisión con otro objeto
        return self.x == other.x and self.y == other.y
    
    def reset(self):
        # Reinicia la posición de la entidad a su valor inicial
        self.x = 0
        self.y = 0

    