from settings import *
from random import randint

class rectangle_obstacle:
    def __init__(self):
        self.color = rect_color
        self.size = 80
        self.position = pygame.math.Vector2((randint(edge_thickness, screen_width - edge_thickness - self.size), randint(edge_thickness + 150, screen_height - edge_thickness - self.size - 150)))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, self.size, self.size), 0)
        img = pygame.image.load('images/box_img.png').convert_alpha()
        img = pygame.transform.scale(img, (self.size, self.size))
        screen.blit(img, (self.position.x, self.position.y))