from player import Player
import pygame
from settings import *

class Bot(Player):
    def __init__(self):
        super().__init__()
        self.startPosition = pygame.math.Vector2(game_screen_width - 25 - self.width, int(game_screen_height / 2) - int(self.height / 2))
        self.position = self.startPosition.copy()
        self.color = 'light blue'

    def update(self, ball):
        if self.cooldown > 0:
            self.cooldown -= 1

        #elif ball.lastPlayerToPlay != 1:
           # pass

        else:
            if ball.position.y > self.position.y + 3*self.height / 4:
                self.position.y += self.velocity
                self.orientation = 1
            elif ball.position.y < self.position.y + self.height / 4:
                self.position.y -= self.velocity
                self.orientation = -1
            else:
                self.orientation = 0

        if self.height_change_timer > 0:
            self.height_change_timer -= 1

        if self.height_change_timer == 1:
            self.height = self.startHeight