import sys
import pygame

pygame.init()

width = 480 #480
height = 755 #720

square_size = 35

floor_y = int((height - 80) / square_size)

right_end_x = int((width - 60) / square_size)
left_end_x = 30

"""fps = 1000
fpsClock = pygame.time.Clock()"""

x_offset = 30
y_offset = 30

font = pygame.font.Font('freesansbold.ttf', 20)