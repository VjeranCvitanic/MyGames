from settings import *
from grid import grid


def main():
    screen = pygame.display.set_mode((width, height))
    screen.fill('black')

    new_grid = grid()

    #new_grid.start(screen)
    new_grid.start_gliders(10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        new_grid.live()

        new_grid.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
