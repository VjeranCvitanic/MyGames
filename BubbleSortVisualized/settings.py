import pygame

pygame.init()

width, height = 640, 480
rect_width = 10

show_speed = 0.001

fps = 60
fpsClock = pygame.time.Clock()
fpsClock.tick(fps)

rect_color = 'light yellow'

background_color = 'black'