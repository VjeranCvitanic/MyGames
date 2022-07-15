import pygame
from settings import *
def countdown(screen, background_color):
    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    run = False
            if e.type == pygame.QUIT:
                run = False

        pygame.draw.rect(screen, background_color,
                         pygame.Rect(game_screen_width / 2 - 20, game_screen_height / 2 - 100 - 10, 50, 50))
        screen.blit(font.render(text, True, 'green'), (game_screen_width / 2 - 10, game_screen_height / 2 - 100))
        pygame.display.flip()