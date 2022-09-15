from settings import *
from copy import deepcopy
from randomTetronimo import randomTetronimo

class Grid:
    def __init__(self):
        self.square_size = square_size
        self.width = width - 60
        self.height = height - 80
        self.num_of_rows = int(self.height / self.square_size)
        self.num_of_cols = int(self.width / self.square_size)
        self.matrix = [[0 for j in range(0, self.num_of_cols)] for i in range(0, self.num_of_rows + 1)]
        self.tetronimoes_list = []
        self.hold_tetronimo = randomTetronimo()
        self.nextTetronimo = 0
        self.score = 0
        self.highscore = 0


    def draw(self, screen):
        for i in range(0, self.width, self.square_size):
            for j in range(0, self.height, self.square_size):
                pygame.draw.rect(screen, 'light yellow', pygame.Rect(i + x_offset, j + y_offset, self.square_size, self.square_size), 1)

        for tet in self.tetronimoes_list:
            tet.draw(screen)

        score_text = font.render('score:' + str(self.score), True, 'orange', 'black')
        screen.blit(score_text, (width - 20, 50))

        highscore_text = font.render('Highscore:', True, 'orange', 'black')
        screen.blit(highscore_text, (width - 20, height - 80))

        highscore_text_2 = font.render(str(self.highscore), True, 'orange', 'black')
        screen.blit(highscore_text_2, (width - 20, height - 50))

        pygame.draw.rect(screen, self.nextTetronimo.color, pygame.Rect(width - 20, 100, 20, 20), 0)

    def check_if_move_is_valid(self, x, y) -> bool:
        if y > 11 or y < 0 or x - 1 >= floor_y or self.matrix[x][y] != 0:
            return False
        if self.matrix[x][y] == 0:
            return True

    def add_to_matrix(self, tetronimo):
        self.score += 10
        for pos in tetronimo.positions_list:
            x = pos[0]
            y = pos[1]
            self.matrix[x][y] = 1

    def check_if_row_is_full(self):
        num_of_full_rows = 0
        for i in range(0, self.num_of_rows + 1):
            flag = True
            for j in range(0, self.num_of_cols):
                if self.matrix[i][j] != 1:
                    flag = False
            if flag:
                num_of_full_rows += 1
                for j in range(0, self.num_of_cols):
                    self.matrix[i][j] = 0
                self.delete_row(i)


        if num_of_full_rows == 0:
            pass
        elif num_of_full_rows == 1:
            self.score += 40
        elif num_of_full_rows == 2:
            self.score += 100
        elif num_of_full_rows == 3:
            self.score += 300
        elif num_of_full_rows == 4:
            self.score += 1200
        else:
            self.score += 1200 + num_of_full_rows * 200

    def delete_row(self, row):
        help_matrix = [[0 for j in range(0, self.num_of_cols)] for i in range(0, self.num_of_rows + 1)]
        for i in range(0, row):
            for j in range(0, self.num_of_cols):
                if self.matrix[i][j] == 1:
                    help_matrix[i + 1][j] = 1

        for i in range(row + 1, self.num_of_rows + 1):
            for j in range(0, self.num_of_cols):
                help_matrix[i][j] = self.matrix[i][j]

        self.matrix = help_matrix


        for tetronimo in self.tetronimoes_list:
            help_list = []
            help_list.clear()
            for pos in tetronimo.positions_list:
                if pos[0] == row:
                    pass
                elif pos[0] < row:
                    x = pos[0]
                    y = pos[1]
                    pos = (x + 1, y)
                    help_list.append(pos)
                else:
                    help_list.append(pos)

            tetronimo.positions_list.clear()
            tetronimo.positions_list = help_list

        """for tetronimo in self.tetronimoes_list:
            self.add_to_matrix(tetronimo)"""


    def check_if_end(self):
        for j in range(0, self.num_of_cols):
            if self.matrix[0][j] != 0:
                if self.score > self.highscore:
                    with open('highscore.txt', 'w') as f:
                        f.write(str(self.score))
                return True

        return False