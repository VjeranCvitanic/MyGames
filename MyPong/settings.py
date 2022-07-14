import pygame
import os

pygame.init()

screen_width = 360
screen_height = 480

game_screen_width = 1080
game_screen_height = 640

background_color_light_mode = 'light yellow'
background_color_dark_mode = 'black'

light_mode_image = pygame.image.load('../MyPong/images/light_mode_icon.jpg')
dark_mode_image = pygame.image.load('../MyPong/images/dark_mode_icon.jpg')

background_color = 'light yellow'
mode_image = pygame.transform.scale(light_mode_image, (90, 80))

light_mode_image = pygame.transform.scale(light_mode_image, (90, 80))
dark_mode_image = pygame.transform.scale(dark_mode_image, (90, 80))


button_color = 'light blue'
dark_button_color = 'dark blue'

color_list = ['green', 'dark blue', 'magenta', 'dark red', 'black', 'brown', 'purple']
fire_color = 'gold'

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 20)

fps = 60
fpsClock = pygame.time.Clock()

x = 300
y = 120
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)