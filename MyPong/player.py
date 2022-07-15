import pygame
from settings import *
from copy import copy

class Player():
    def __init__(self):
        self.width = 15
        self.startHeight = 100
        self.height = copy(self.startHeight)
        #self.velocity = 3.9
        self.velocity = 7
        self.orientation = 1
        self.score = 0
        self.cooldown = 0
        self.height_change_timer = 0
        self.startPosition = 0
        self.position = 0
        self.color = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, self.width, self.height))


class Player1(Player):
    def __init__(self):
        super().__init__()
        self.startPosition = pygame.math.Vector2(25, int(game_screen_height / 2) - int(self.height / 2))
        self.position = self.startPosition.copy()
        self.color = 'red'

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1

        else:
            key = pygame.key.get_pressed()

            if key[pygame.K_w] and self.position.y > 0:
                self.position.y -= self.velocity
                self.orientation = -1
            elif key[pygame.K_s] and self.position.y < game_screen_height - self.height:
                self.position.y += self.velocity
                self.orientation = 1
            else:
                self.orientation = 0

        if self.height_change_timer > 0:
            self.height_change_timer -= 1

        elif self.height_change_timer == 1:
            self.height = self.startHeight


class Player2(Player):
    def __init__(self):
        super().__init__()
        self.startPosition = pygame.math.Vector2(game_screen_width - 25 - self.width, int(game_screen_height / 2) - int(self.height / 2))
        self.position = self.startPosition.copy()
        self.color = 'blue'

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            key = pygame.key.get_pressed()

            if key[pygame.K_UP] and self.position.y > 0:
                self.position.y -= self.velocity
                self.orientation = -1
            elif key[pygame.K_DOWN] and self.position.y < game_screen_height - self.height:
                self.position.y += self.velocity
                self.orientation = 1
            else:
                self.orientation = 0

        if self.height_change_timer > 0:
            self.height_change_timer -= 1

        if self.height_change_timer == 1:
            self.height = self.startHeight


class DoubleModePlayer(Player):
    def __init__(self):
        super().__init__()
        self.width = 300
        self.height = 15


class DoubleModePlayer1(DoubleModePlayer):
    def __init__(self):
        super().__init__()
        self.startPosition = pygame.math.Vector2(int(game_screen_width / 2) - int(self.width / 2), 25)
        self.position = self.startPosition.copy()
        self.color = 'pink'

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a] and self.position.x > 0:
            self.position.x -= self.velocity
            self.orientation = -1
        elif key[pygame.K_d] and self.position.x < game_screen_width - self.width:
            self.position.x += self.velocity
            self.orientation = 1
        else:
            self.orientation = 0



class DoubleModePlayer2(DoubleModePlayer):
    def __init__(self):
        super().__init__()
        self.startPosition = pygame.math.Vector2(int(game_screen_width / 2) - int(self.width / 2), game_screen_height - 25)
        self.position = self.startPosition.copy()
        self.color = 'light blue'

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.position.x > 0:
            self.position.x -= self.velocity
            self.orientation = -1
        elif key[pygame.K_RIGHT] and self.position.x < game_screen_width - self.width:
            self.position.x += self.velocity
            self.orientation = 1
        else:
            self.orientation = 0