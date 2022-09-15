import sys
from settings import *

from Array import Array


def main():
    screen = pygame.display.set_mode((width, height))

    new_array = Array()



    while True:
        screen.fill(background_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        j = new_array.BubbleSort(screen)
        new_array.draw(screen, j)


        pygame.display.flip()
        fpsClock.tick(fps)


main()
