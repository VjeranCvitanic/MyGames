import pygame
from random import randint, choice
from settings import *

class PowerUps:
    def __init__(self):
        self.position = pygame.math.Vector2((randint(120, game_screen_width - 120)), randint(40, game_screen_height - 40))
        self.size = 40
        self.image = pygame.Surface((self.size, self.size))
        self.alive = False
        self.type = choice(['sizex2', 'size/2', 'ballspeedx2', 'freezeopponent1s'])

        if self.type == 'ballspeedx2':
            self.image = pygame.image.load('../MyPong/images/fire_icon.png').convert_alpha()
        elif self.type == 'freezeopponent1s':
            self.image = pygame.image.load('../MyPong/images/freeze_icon.png').convert_alpha()
        elif self.type == 'sizex2':
            self.image = pygame.image.load('../MyPong/images/lengthx2.png').convert_alpha()
        elif self.type == 'size/2':
            self.image = pygame.image.load('../MyPong/images/length0,5.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.size, self.size))


    def draw(self, screen, background_color):
        if self.alive:
            #pygame.draw.rect(screen, background_color, pygame.Rect(self.position.x, self.position.y, self.size, self.size), 0)
            screen.blit(self.image, (self.position.x, self.position.y, self.size, self.size))

