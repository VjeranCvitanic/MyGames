import pygame
from settings import *
from random import choice
from numpy import sign

class Ball():
    def __init__(self):
        self.color = choice(color_list)

        self.radius = 7
        self.speed = 14

        self.lastPlayerToPlay = -1
        self.previous_positions = []

        if choice([-1,1]) == 1:
            self.velocity = pygame.math.Vector2(self.speed, 3.1 * choice((-1, 0, 1)))
            self.position = pygame.math.Vector2(int(game_screen_width / 2) - 400, int(game_screen_height / 2))

        else:
            self.velocity = pygame.math.Vector2(-1 * self.speed, 3.1 * choice((-1, 0, 1)))
            self.position = pygame.math.Vector2(int(game_screen_width / 2) + 400, int(game_screen_height / 2))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0)
        if len(self.previous_positions) <= 10:
            pygame.draw.polygon(screen, fire_color, [(self.position.x - 5*sign(self.velocity.x), self.position.y + self.radius - 1),
                                                     (self.previous_positions[0].x, self.previous_positions[0].y),
                                                     (self.position.x - 5*sign(self.velocity.x), self.position.y - self.radius - 1)],
                                                     0)

        else:
            pygame.draw.polygon(screen, fire_color, [(self.position.x - 5*sign(self.velocity.x), self.position.y + self.radius - 1),
                                                     (self.previous_positions[len(self.previous_positions) - 10 - 1].x,
                                                      self.previous_positions[len(self.previous_positions) - 10 - 1].y),
                                                     (self.position.x - 5*sign(self.velocity.x), self.position.y - self.radius + 1)],
                                                     0)






    def update(self):
        self.previous_positions.append(self.position.copy())
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

