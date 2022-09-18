from settings import *
from grid import Grid
from randomTetronimo import randomTetronimo
import os
from copy import deepcopy
from random import choice
os.environ["SDL_VIDEODRIVER"] = "dummy"


"""
Some alternative rotations become buggy sometimes
"""


def main():
    pygame.init()
    screen = pygame.display.set_mode((width + 100, height))
    new_grid = Grid()
    new_tetronimo = randomTetronimo()

    new_grid.nextTetronimo = randomTetronimo()
    new_grid.tetronimoes_list.append(new_tetronimo)

    key_get_pressed_timer = 1
    fall_timer = 400 #330
    speed_up_the_game_timer = 1
    speed_up_the_game_mod = 55000
    speed_up_factor = 5
    sensitivity = 70

    pygame.display.set_caption('Tetris')
    icon_img = pygame.image.load('tetris_icon.jpg').convert_alpha()
    pygame.display.set_icon(icon_img)

    with open('highscore.txt') as f:
        highscore = f.readlines()

    for line in highscore:
        new_grid.highscore = int(line)


    run = True
    end = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                new_tetronimo.rotate(new_grid)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                new_tetronimo.fallDownFast(new_grid)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                return_value = new_tetronimo.hold(new_grid)
                if return_value != 0:
                    new_tetronimo = return_value
                    new_tetronimo.positions_list = deepcopy(new_tetronimo.startPositions_list)
                    new_grid.tetronimoes_list.append(new_tetronimo)
            elif event.type == pygame.KEYUP and event.key == pygame.K_p:
                pause_flag = True
                while pause_flag:
                    pause_img = pygame.image.load("pause_img.jpg").convert_alpha()
                    picture = pygame.transform.scale(pause_img, (80, 80))
                    screen.blit(picture, (width / 2 - 40, height / 2 - 40))

                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            pause_flag = False
                    pygame.display.flip()


        if key_get_pressed_timer % sensitivity == 0:
            screen.fill('black')
            new_grid.draw(screen)
            key = pygame.key.get_pressed()
            new_tetronimo.update(key, new_grid)



        if key_get_pressed_timer % fall_timer == 0:
            if speed_up_the_game_timer % speed_up_the_game_mod == 0:
                fall_timer = fall_timer - speed_up_factor
                if fall_timer < 250:
                    speed_up_factor = 3
                elif fall_timer < 100:
                    speed_up_factor = 0
                speed_up_the_game_timer = 1
                if sensitivity < 62:
                    sensitivity -= 2
                elif sensitivity < 58:
                    pass
                else:
                    sensitivity -= 4
                new_grid.level += 1
                new_grid.lvl_color = choice(['purple', 'blue', 'light blue', 'yellow', 'orange', 'red', 'pink', 'light green'])

            speed_up_the_game_timer += 1
            screen.fill('black')
            new_grid.draw(screen)
            new_tetronimo.fall(new_grid)

        key_get_pressed_timer += 1
        if speed_up_the_game_timer % speed_up_the_game_mod != 0:
            speed_up_the_game_timer += 1

        else:
            speed_up_the_game_timer = 0



        if not new_tetronimo.falling:
            new_grid.add_to_matrix(new_tetronimo)
            new_grid.check_if_row_is_full()
            if new_grid.check_if_end():
                f = True
                while f:
                    pygame.draw.rect(screen, 'black', pygame.Rect(width / 2 - 60, height / 2 - 10, 108, 40), 0)
                    score_txt = font.render('score:' + str(new_grid.score), True, 'orange', 'black')
                    screen.blit(score_txt, (width / 2 - 55, height / 2 - 2))
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            f = False
                    pygame.display.flip()

                run = False
                pygame.quit()
                sys.exit()


            new_tetronimo = new_grid.nextTetronimo
            new_grid.nextTetronimo = randomTetronimo()
            new_grid.tetronimoes_list.append(new_tetronimo)

        pygame.display.flip()




if __name__ == '__main__':
    main()
