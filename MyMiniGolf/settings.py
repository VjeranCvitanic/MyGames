import pygame
screen_width = 520
screen_height = 712

pygame.init()

background_color = 'light green'
light_green = (0, 255, 0)
dark_green = (0, 153, 0)

rect_color = 'brown'

fps = 60
fpsClock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 20)

edge_thickness = 20

button_color = 'dark green'

friction_mi = 0.1
g = 9.81

friction = g * friction_mi

energy_loss_factor = 0.7

bunker_loss = 0.01