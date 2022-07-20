import sys
from settings import *
from play import level1, level2

#portali, bunkeri, water hazard, uzvisine
#modulirat kod

def main():
    screen = pygame.display.set_mode((screen_width, screen_height))

    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if 20 <= mouse_position[0] <= 78 and 50 <= mouse_position[1] <= 70:
                    level1()
                if 20 <= mouse_position[0] <= 78 and 80 <= mouse_position[1] <= 100:
                    level2()

        screen.fill(background_color)

        main_text = font.render('level1', True, 'blue', button_color)
        screen.blit(main_text, (20, 50))

        main_text2 = font.render('level2', True, 'blue', button_color)
        screen.blit(main_text2, (20, 80))


        pygame.display.flip()
        fpsClock.tick(fps)



if __name__ == '__main__':
    main()