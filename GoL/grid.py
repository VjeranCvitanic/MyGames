from settings import *
from copy import deepcopy

class square():
    def __init__(self, i = 0, j = 0):
        self.alive = False
        self.size = square_size
        self.i = i
        self.j = j

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, 'light yellow', pygame.Rect(self.i * self.size, self.j * self.size, self.size - 1, self.size - 1), 0)
        else:
            pygame.draw.rect(screen, 'black', pygame.Rect(self.i * self.size, self.j * self.size, self.size - 1, self.size - 1), 0)

class grid:
    def __init__(self):
        self.square_size = square_size
        self.number_of_rows = int(height / self.square_size)
        self.number_of_columns = int(width / self.square_size)
        self.squares_matrix = [[0 for j in range(self.number_of_rows)] for i in range(self.number_of_columns)]
        self.prev_state_matrix = [[0 for j in range(self.number_of_rows)] for i in range(self.number_of_columns)]

        for i in range(self.number_of_columns):
            for j in range(self.number_of_rows):
                new_square = square(i, j)
                self.squares_matrix[i][j] = new_square
                self.prev_state_matrix[i][j] = deepcopy(new_square)

    def draw(self, screen):
        for i in range(self.number_of_columns):
            for j in range(self.number_of_rows):
                pygame.draw.rect(screen, 'light yellow', pygame.Rect(i * self.square_size, j * self.square_size, self.square_size, self.square_size), 1)
                self.squares_matrix[i][j].draw(screen)

    def start(self, screen):
        run = True
        while run:
            self.draw(screen)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                run = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()

                    x = int(int(mouse_position[0]) / self.square_size)
                    y = int(int(mouse_position[1]) / self.square_size)

                    self.squares_matrix[x][y].alive = not self.squares_matrix[x][y].alive
            pygame.display.flip()
        self.prev_state_matrix = deepcopy(self.squares_matrix)


    def live(self):
        for i in range(self.number_of_columns):
            for j in range(self.number_of_rows):
                counter = self.live_neighbours(i, j)
                if counter < 2 or counter > 3:
                    self.squares_matrix[i][j].alive = False
                elif counter == 3:
                    self.squares_matrix[i][j].alive = True

        self.prev_state_matrix = deepcopy(self.squares_matrix)


    def live_neighbours(self, i, j):
        counter = 0
        for i_offset in range(-1,2):
            for j_offset in range(-1, 2):
                if i_offset == 0 and j_offset == 0:
                    pass
                else:
                    if 0 <= i + i_offset < self.number_of_columns and 0 <= j + j_offset < self.number_of_rows:
                         if self.prev_state_matrix[i + i_offset][j + j_offset].alive:
                            counter += 1
        return counter

    def draw_block(self, i, j):
        if 0 <= i < self.number_of_columns - 2 and 0 <= j < self.number_of_rows - 2:
            self.squares_matrix[i][j].alive = True
            self.squares_matrix[i + 1][j + 1].alive = True
            self.squares_matrix[i][j + 1].alive = True
            self.squares_matrix[i + 1][j].alive = True

    def start_gliders(self, i, j):
        if 0 <= i < self.number_of_columns - 35 and 4 <= j < self.number_of_rows - 5:
            self.draw_block(i, j)

            self.squares_matrix[i + 10][j].alive = True
            self.squares_matrix[i + 10][j + 1].alive = True
            self.squares_matrix[i + 10][j + 2].alive = True
            self.squares_matrix[i + 11][j - 1].alive = True
            self.squares_matrix[i + 11][j + 3].alive = True
            self.squares_matrix[i + 12][j - 2].alive = True
            self.squares_matrix[i + 13][j - 2].alive = True
            self.squares_matrix[i + 12][j + 4].alive = True
            self.squares_matrix[i + 13][j + 4].alive = True

            self.squares_matrix[i + 14][j + 1].alive = True

            self.squares_matrix[i + 15][j - 1].alive = True
            self.squares_matrix[i + 15][j + 3].alive = True

            self.squares_matrix[i + 16][j].alive = True
            self.squares_matrix[i + 16][j + 1].alive = True
            self.squares_matrix[i + 16][j + 2].alive = True

            self.squares_matrix[i + 17][j + 1].alive = True

            self.draw_block(i + 20, j - 2)
            self.squares_matrix[i + 20][j].alive = True
            self.squares_matrix[i + 21][j].alive = True

            self.squares_matrix[i + 22][j - 3].alive = True
            self.squares_matrix[i + 22][j + 1].alive = True

            self.squares_matrix[i + 24][j - 3].alive = True
            self.squares_matrix[i + 24][j - 4].alive = True

            self.squares_matrix[i + 24][j + 1].alive = True
            self.squares_matrix[i + 24][j + 2].alive = True

            self.draw_block(i + 34, j - 2)

        self.prev_state_matrix = deepcopy(self.squares_matrix)




