from player import Player1, Player2, DoubleModePlayer2, DoubleModePlayer1
from ball import Ball
from check_collision import check_collision
from settings import *
from print_score import print_score
from win import check_if_win
from bot import Bot
from countdown import countdown

def mode(game_mode, background_color, against_bot):
    pygame.init()

    screen = pygame.display.set_mode((game_screen_width, game_screen_height))
    if game_mode == 'normal':
        pygame.display.set_caption('Normal Mode')
    elif game_mode == 'survival':
        pygame.display.set_caption('Survival Mode')
    elif game_mode == 'random':
        pygame.display.set_caption('Random Mode')
    elif game_mode == 'double':
        pygame.display.set_caption('Double Mode')

    powerUps_list = []

    p1 = Player1()

    if not against_bot:
        p2 = Player2()
    else:
        p2 = Bot()

    ball = Ball()

    goal = False

    if game_mode == 'double':
        p1_2 = DoubleModePlayer1()
        p2_2 = DoubleModePlayer2()



    screen.fill(background_color)
    p1.draw(screen)
    p2.draw(screen)

    if game_mode == 'double':
        p1_2.draw(screen)
        p2_2.draw(screen)


    countdown(screen, background_color)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        if game_mode == 'double':
            if check_collision(ball, p1, p2, game_mode, powerUps_list, p1_2, p2_2) == 'goal':
                goal = True

        else:
            if check_collision(ball, p1, p2, game_mode, powerUps_list) == 'goal':
                goal = True

        ball.update()

        p1.update()
        if not against_bot:
            p2.update()
        else:
            p2.update(ball)

        if game_mode == 'double':
            p1_2.update()
            p2_2.update()


        screen.fill(background_color)

        p1.draw(screen)
        p2.draw(screen)
        if game_mode == 'double':
            p1_2.draw(screen)
            p2_2.draw(screen)
        ball.draw(screen)
        print_score(screen, p1, p2)

        if check_if_win(p1, p2):
            return

        if goal:
            countdown(screen, background_color)
            goal = False

        for powerUp in powerUps_list:
            powerUp.draw(screen, background_color)


        pygame.display.flip()
        fpsClock.tick(fps)