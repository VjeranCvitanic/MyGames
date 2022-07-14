import pygame
from settings import *
from random import randint, choice
from numpy import sign
from power_ups import PowerUps


def check_collision(ball, player1, player2, game_mode, powerUps_list):
    #collision with paddles
    if ball.position.x + ball.radius >= player2.position.x and player2.position.y + player2.height >= ball.position.y - ball.radius and ball.position.y + ball.radius >= player2.position.y:
        ball.velocity.x *= -1
        ball.lastPlayerToPlay = 2
        ball.velocity.y -= player2.orientation * player2.velocity * 0.5
        if game_mode == 'normal' and randint(1,3) == 1:
            powerUp = PowerUps()
            powerUp.alive = True
            powerUps_list.append(powerUp)
        elif game_mode == 'random':
            powerUp = PowerUps()
            powerUp.alive = True
            powerUps_list.append(powerUp)
            ball.speed = randint(9,17)
            ball.velocity.x = sign(ball.velocity.x) * ball.speed

    elif ball.position.x - ball.radius <= player1.position.x + player1.width and player1.position.y + player1.height >= ball.position.y - ball.radius and ball.position.y + ball.radius >= player1.position.y:
        ball.velocity.x *= -1
        ball.lastPlayerToPlay = 1
        ball.velocity.y -= player1.orientation * player1.velocity * 0.5
        if game_mode == 'normal' and randint(1,3) == 1:
            powerUp = PowerUps()
            powerUp.alive = True
            powerUps_list.append(powerUp)
        elif game_mode == 'random':
            powerUp = PowerUps()
            powerUp.alive = True
            powerUps_list.append(powerUp)
            ball.speed = randint(9,17)
            ball.velocity.x = sign(ball.velocity.x) * ball.speed


    # checks if ball hits base or top of a player -> needs work
    elif ball.position.x - ball.radius <= player1.position.x + player1.width and ball.position.x + ball.radius >= player1.position.x:
        if ball.position.y - ball.radius <= player1.position.y + player1.height and ball.position.y + ball.radius >= player1.position.y:
            ball.velocity.y *= -1

    elif ball.position.x - ball.radius >= player2.position.x + player2.width and ball.position.x + ball.radius <= player2.position.x:
        if ball.position.y - ball.radius <= player2.position.y + player2.height and ball.position.y + ball.radius >= player2.position.y:
            ball.velocity.y *= -1


    #checks floor and ceiling
    elif ball.position.y + ball.radius >= game_screen_height:
        ball.position.y = game_screen_height - ball.radius
        ball.velocity.y *= -1
        if game_mode == 'random':
            ball.speed = randint(9, 17)
            ball.velocity.y = float(choice([-1, -1, -1, -1, -1, 1])) * (ball.speed - 4)
            if choice([-1, -1, -1, -1, -1, -1, -1, -1, 1]) == 1:
                ball.position.y = ball.radius

    elif ball.position.y - ball.radius <= 0:
        ball.position.y = ball.radius
        ball.velocity.y *= -1
        if game_mode == 'random':
            ball.speed = randint(9, 17)
            ball.velocity.y *= float(choice([-1, -1, -1, -1, -1, 1])) * (ball.speed - 4)
            if choice([-1, -1, -1, -1, -1, -1, -1, -1, 1]) == 1:
                ball.position.y = game_screen_height - ball.radius


    #goal
    elif ball.position.x + ball.radius >= game_screen_width:
        player1.score += 1
        ball.__init__()
        player1.position = player1.startPosition.copy()
        player2.position = player2.startPosition.copy()
        if game_mode == 'survival':
            player1.height = player1.height / 1.8
            player1.width = player1.width / 1.2
        elif game_mode == 'random':
            ball.speed = randint(9,17)
            player1.height = randint(25, 180)
            player2.height = randint(25, 180)
            player1.position.y = choice([player1.startPosition.y, player1.position.y, randint(player1.height, game_screen_height - player1.height)])
        elif game_mode == 'normal':
            player1.height = player1.startHeight
            player1.cooldown = 0
            player1.height_change_timer = 0

            player2.height = player2.startHeight
            player2.cooldown = 0
            player2.height_change_timer = 0

            powerUps_list.clear()

    elif ball.position.x - ball.radius <= 0:
        player2.score += 1
        ball.__init__()
        player1.position = player1.startPosition.copy()
        player2.position = player2.startPosition.copy()
        if game_mode == 'survival':
            player2.height = player2.height / 1.8
            player2.width = player2.width / 1.2
        elif game_mode == 'random':
            ball.speed = randint(9,17)
            player1.height = randint(25, 180)
            player2.height = randint(25, 180)
            player1.position.y = choice([player1.startPosition.y, player1.position.y, randint(player1.height, game_screen_height - player1.height)])
        elif game_mode == 'normal':
            player1.height = player1.startHeight
            player1.cooldown = 0
            player1.height_change_timer = 0

            player2.height = player2.startHeight
            player2.cooldown = 0
            player2.height_change_timer = 0

            powerUps_list.clear()


    for each_powerUp in powerUps_list:
        if ball.position.x - ball.radius <= each_powerUp.position.x + each_powerUp.size and ball.position.x + ball.radius >= each_powerUp.position.x and ball.position.y - ball.radius <= each_powerUp.position.y + each_powerUp.size and ball.position.y + ball.radius >= each_powerUp.position.y:
            if each_powerUp.type == 'sizex2':
                if ball.lastPlayerToPlay == 1:
                    player1.height *= 2
                    player1.height_change_timer = 8 * fps
                elif ball.lastPlayerToPlay == 2:
                    player2.height *= 2
                    player2.height_change_timer = 8 * fps

            elif each_powerUp.type == 'size/2':
                if ball.lastPlayerToPlay == 1:
                    player1.height /= 2
                    player1.height_change_timer = 8 * fps
                elif ball.lastPlayerToPlay == 2:
                    player2.height /= 2
                    player2.height_change_timer = 8 * fps

            elif each_powerUp.type == 'ballspeedx2':
                ball.velocity.x *= 1.6
                ball.velocity.y *= 1.6

            elif each_powerUp.type == 'freezeopponent1s':
                if ball.lastPlayerToPlay == 1:
                    player2.cooldown = 2 * fps
                elif ball.lastPlayerToPlay == 2:
                    player1.cooldown = 2 * fps

            powerUps_list.remove(each_powerUp)
            each_powerUp.alive = False