from settings import *
from random import randint

class Bunker:
    def __init__(self):
        self.color = 'light yellow'
        self.radius1 = randint(12, 25)
        self.radius2 = randint(12 ,25)

        self.position1 = pygame.math.Vector2((randint(edge_thickness + 50, screen_width - edge_thickness - self.radius1 - 50), randint(edge_thickness + 150, screen_height - edge_thickness - self.radius1 - 150)))
        self.position2 = pygame.math.Vector2((randint(int(self.position1.x - self.radius1), int(self.position1.x + self.radius1)), randint(int(self.position1.y - self.radius1), int(self.position1.y + self.radius1))))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position1.x, self.position1.y), self.radius1, 0)
        pygame.draw.circle(screen, self.color, (self.position2.x, self.position2.y), self.radius2, 0)
