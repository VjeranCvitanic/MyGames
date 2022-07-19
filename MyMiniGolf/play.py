from settings import *
from ball import Ball
from copy import copy
from rectangle_obstacle import rectangle_obstacle
from bunker import Bunker
from water_hazard import Water_hazard

def level1():
    screen = pygame.display.set_mode((screen_width, screen_height))
    ball = Ball()

    startPos = -1

    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and ball.position.x - ball.radius <= mouse_position[0] <= ball.position.x + ball.radius and ball.position.y - ball.radius <= mouse_position[1] <= ball.position.y + ball.radius:
                startPos = mouse_position

            if event.type == pygame.MOUSEBUTTONUP and startPos != -1:
                endPos = pygame.mouse.get_pos()
                ball.shoot(startPos, endPos)
                startPos = -1


        screen.fill(dark_green)
        counter = 1
        for x in range(21, screen_width - 20, 32):
            br = counter
            counter += 1
            for y in range(21, screen_height - 20, 32):
                br += 1
                if br % 2 == 0:
                    pygame.draw.rect(screen, light_green, pygame.Rect(x, y, 32, 32), 0)




        pygame.draw.rect(screen, (70, 0, 0), pygame.Rect(0, 0, screen_width, screen_height), edge_thickness)
        pygame.draw.circle(screen, (0,0,0), (screen_width / 2 - 5, 80), 10, 0)
        if ball.update() == 'goal':
            level2()
        ball.draw(screen)

        prev = copy(ball.position)
        for pos in ball.prevPositions:
            pygame.draw.circle(screen, (0, 0, 0), pos, 1, 0)
            pygame.draw.line(screen, (255,255,255), prev, pos, 2)
            prev = copy(pos)

        if startPos != -1:
            pygame.draw.line(screen, 'orange', ball.position, mouse_position, 4)

        pygame.display.flip()
        fpsClock.tick(fps)

def level2():
    screen = pygame.display.set_mode((screen_width, screen_height))
    ball = Ball()

    startPos = -1

    box_list = []
    bunker_list = []
    water_list = []

    for i in range(0, 6):
        bunker = Bunker()
        bunker_list.append(bunker)

    for i in range(0, 4):
        rect = rectangle_obstacle()
        box_list.append(rect)

    for i in range(0, 3):
        water = Water_hazard()
        water_list.append(water)

    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and ball.position.x - ball.radius <= mouse_position[
                0] <= ball.position.x + ball.radius and ball.position.y - ball.radius <= mouse_position[
                1] <= ball.position.y + ball.radius:
                startPos = mouse_position

            if event.type == pygame.MOUSEBUTTONUP and startPos != -1:
                mouse_position = pygame.mouse.get_pos()
                endPos = mouse_position
                ball.shoot(startPos, endPos)
                startPos = -1

        screen.fill(dark_green)
        counter = 1
        for x in range(21, screen_width - 20, 32):
            br = counter
            counter += 1
            for y in range(21, screen_height - 20, 32):
                br += 1
                if br % 2 == 0:
                    pygame.draw.rect(screen, light_green, pygame.Rect(x, y, 32, 32), 0)


        pygame.draw.rect(screen, (70, 0, 0), pygame.Rect(0, 0, screen_width, screen_height), edge_thickness)

        pygame.draw.circle(screen, (0, 0, 0), (screen_width / 2 - 5, 80), 10, 0)
        if ball.update() == 'goal':
            level2()

        for water in water_list:
            water.draw(screen)
            ball.water_collision(water)

        for bunker in bunker_list:
            bunker.draw(screen)
            ball.bunker_collision(bunker)

        for rect in box_list:
            rect.draw(screen)
            ball.box_collision(rect)

        ball.draw(screen)

        prev = copy(ball.position)
        for pos in ball.prevPositions:
            pygame.draw.circle(screen, (0,0,0), pos, 1, 0)
            pygame.draw.line(screen, (255, 255, 255), prev, pos, 2)
            prev = copy(pos)

        if startPos != -1:
            pygame.draw.line(screen, 'orange', ball.position, mouse_position, 4)

        pygame.display.flip()
        fpsClock.tick(fps)



#        if startPos != -1:
            #point1 = [startPos[0], startPos[1]]
            #point2 = [mouse_position[0] + 5, mouse_position[1] + 5]
            #point3 = [mouse_position[0] - 5, mouse_position[1] - 5]

            #if abs(mouse_position[0] - startPos[0]) > 50:
             #   print(abs(mouse_position[0] - startPos[0]))
              #  if mouse_position[0] > startPos[0]:
               #     point2[0] = startPos[0] + 50
                #    point3[0] = startPos[0] + 50
                #else:
                 #   point2[0] = startPos[0] - 50
                  #  point3[0] = startPos[0] - 50
            #if abs(mouse_position[1] - startPos[1]) > 50:
             #   if mouse_position[1] > startPos[1]:
              #      point2[1] = startPos[1] + 50
               #     point3[1] = startPos[1] + 50
                #else:
                 #   point2[1] = startPos[1] - 50
                  #  point3[1] = startPos[1] - 50
            #if abs(mouse_position[0] - startPos[0]) < 8 and abs(mouse_position[1] - startPos[1]) < 8:
             #   point2[0] = startPos[0]
              #  point2[1] = startPos[1]
               # point3[0] = startPos[0]
                #point3[1] = startPos[1]


            #pygame.draw.polygon(screen, 'orange', [point1, point2, point3], 0)