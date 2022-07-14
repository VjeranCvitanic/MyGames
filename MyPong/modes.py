from player import Player1, Player2
from ball import Ball
from check_collision import check_collision
from settings import *
from print_score import print_score
from win import check_if_win

def mode(game_mode, background_color):
    pygame.init()

    screen = pygame.display.set_mode((game_screen_width, game_screen_height))
    if game_mode == 'normal':
        pygame.display.set_caption('Normal Mode')
    elif game_mode == 'survival':
        pygame.display.set_caption('Survival Mode')
    elif game_mode == 'random':
        pygame.display.set_caption('Random Mode')

    powerUps_list = []

    p1 = Player1()

    p2 = Player2()

    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if check_if_win(p1, p2):
            return

        check_collision(ball, p1, p2, game_mode, powerUps_list)

        p1.update()
        p2.update()
        ball.update()

        screen.fill(background_color)

        p1.draw(screen)
        p2.draw(screen)
        ball.draw(screen)

        for powerUp in powerUps_list:
            powerUp.draw(screen)

        print_score(screen, p1, p2)

        pygame.display.flip()
        fpsClock.tick(fps)