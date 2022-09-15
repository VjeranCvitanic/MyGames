from settings import *
from grid import Grid
from randomTetronimo import randomTetronimo
import os
from copy import deepcopy
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
    speed_up_the_game_mod = 18000
    speed_up_factor = 0.96

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


        if key_get_pressed_timer % 80 == 0:
            screen.fill('black')
            new_grid.draw(screen)
            key = pygame.key.get_pressed()
            return_value = new_tetronimo.update(key, new_grid)
            if return_value != 0:
                new_tetronimo = return_value
                new_tetronimo.positions_list = deepcopy(new_tetronimo.startPositions_list)
                new_grid.tetronimoes_list.append(new_tetronimo)
                """if return_value == -1:
                    new_tetronimo = randomTetronimo()
                    new_grid.tetronimoes_list.append(new_tetronimo)
                else:
                    new_tetronimo = return_value
                    new_tetronimo.positions_list = deepcopy(new_tetronimo.startPositions_list)
                    new_grid.tetronimoes_list.append(new_tetronimo)"""

        if key_get_pressed_timer % fall_timer == 0:
            if speed_up_the_game_timer % speed_up_the_game_mod == 0:
                fall_timer = int(fall_timer * speed_up_factor)
                speed_up_the_game_timer = 1
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
                run = False
                pygame.quit()
                sys.exit()


            new_tetronimo = new_grid.nextTetronimo
            new_grid.nextTetronimo = randomTetronimo()
            new_grid.tetronimoes_list.append(new_tetronimo)

        pygame.display.flip()




if __name__ == '__main__':
    main()
