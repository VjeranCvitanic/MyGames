from settings import *

from copy import deepcopy

class Tetronimo:
    def __init__(self):
        self.square_size = square_size
        self.positions_list = []
        self.falling = True
        self.sliding = True
        self.color = 'light yellow'
        self.wasHolded = False

    def draw(self, screen):
        for pos in self.positions_list:
            pygame.draw.rect(screen, self.color,
                             pygame.Rect(pos[1] * self.square_size + x_offset, pos[0] * self.square_size + y_offset,
                                         self.square_size, self.square_size), 0)
            pygame.draw.rect(screen,'light yellow',
                             pygame.Rect(pos[1] * self.square_size + x_offset, pos[0] * self.square_size + y_offset,
                                         self.square_size, self.square_size), 2)

    def fall(self, grid):
        if self.falling:
            new_list = []
            for pos in self.positions_list:
                x = pos[0]
                y = pos[1]
                if not grid.check_if_move_is_valid(x + 1, y):
                    """if x >= floor_y or grid.matrix[x + 1][y] != 0:
                        self.falling = False"""
                    if x >= floor_y or grid.matrix[x + 1][y] != 0:
                        self.falling = False
                    """if x > 0:
                        self.sliding = False"""

                new_list.append((x + 1, y))
            if self.falling:
                self.positions_list = new_list

    def fallDownFast(self, grid):
        while self.falling:
            new_list = []
            for pos in self.positions_list:
                x = pos[0]
                y = pos[1]
                if not grid.check_if_move_is_valid(x + 1, y):
                    if x >= floor_y or grid.matrix[x + 1][y] != 0:
                        self.falling = False

                new_list.append((x + 1, y))
            if self.falling:
                self.positions_list = new_list

    def update(self, key, grid):
        if self.sliding:
            if key[pygame.K_LEFT]:
                flag = False
                new_list = []
                for pos in self.positions_list:
                    x = pos[0]
                    y = pos[1]
                    if not grid.check_if_move_is_valid(x, y - 1):
                        flag = True
                    new_list.append((x, y - 1))
                if not flag:
                    self.positions_list = new_list
                return 0

            if key[pygame.K_RIGHT]:
                flag = False
                new_list = []
                for pos in self.positions_list:
                    x = pos[0]
                    y = pos[1]
                    if not grid.check_if_move_is_valid(x, y + 1):
                        flag = True
                    new_list.append((x, y + 1))
                if not flag:
                    self.positions_list = new_list
                return 0

        if self.falling:
            if key[pygame.K_DOWN]:
                flag = False
                new_list = []
                for pos in self.positions_list:
                    x = pos[0]
                    y = pos[1]
                    if not grid.check_if_move_is_valid(x + 1, y):
                        flag = True
                    new_list.append((x + 1, y))
                if not flag:
                    self.positions_list = new_list
                return 0

            """if key[pygame.K_UP]:
                self.rotate(grid)
                return 0"""

            if key[pygame.K_h] and not self.wasHolded:
                self.wasHolded = True
                old_tetronimo = grid.hold_tetronimo
                grid.hold_tetronimo = self
                grid.tetronimoes_list.remove(self)
                return old_tetronimo


        return 0


class StraightTetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(1, 4), (1, 5), (1, 6), (1, 7)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'light blue'
        self.rotated = False

    def rotate(self, grid):
        if self.rotated:
            new_list = []
            flag = False

            pos1 = self.positions_list[0]
            x = pos1[0]
            y = pos1[1]

            for i in range(-2, 2):
                if grid.check_if_move_is_valid(x + 2, y + i):
                    new_list.append((x + 2, y + i))
                else:
                    flag = True

            if flag:
                flag = False
                for i in range(-2, 2):
                    if grid.check_if_move_is_valid(x + 2, y + i + 2):
                        new_list.append((x + 2, y + i + 2))
                    else:
                        flag = True

            if flag:
                flag = False
                for i in range(-2, 2):
                    if grid.check_if_move_is_valid(x + 2, y + i - 1):
                        new_list.append((x + 2, y + i - 1))
                    else:
                        flag = True

            if not flag:
                self.positions_list = new_list
                self.rotated = not self.rotated


        else:
            new_list = []
            flag = False

            pos1 = self.positions_list[0]
            x = pos1[0]
            y = pos1[1]

            for i in range(-2, 2):
                if grid.check_if_move_is_valid(x + i, y + 2):
                    new_list.append((x + i, y + 2))
                else:
                    flag = True

            if flag:
                flag = False
                for i in range(-2, 2):
                    if grid.check_if_move_is_valid(x + i, y + 4):
                        new_list.append((x + i, y + 4))
                    else:
                        flag = True

            if flag:
                flag = False
                for i in range(-2, 2):
                    if grid.check_if_move_is_valid(x + i, y - 2):
                        new_list.append((x + i, y - 2))
                    else:
                        flag = True

            if not flag:
                self.positions_list = new_list
                self.rotated = not self.rotated


class SquareTetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(0, 5), (0, 6), (1, 5), (1, 6)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'yellow'

    def rotate(self, grid):
        pass


class LTetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(0, 6), (1, 4), (1, 5), (1, 6)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'orange'
        self.state = 0

    def rotate(self, grid):
        if self.state == 0:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[3]
            new_pos.append((axis[0] - 2, axis[1]))
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[3]
                new_pos.append((axis[0] - 2, axis[1] - 2))
                new_pos.append((axis[0] - 1, axis[1] - 2))
                new_pos.append((axis[0], axis[1] - 1))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] - 2):
                        self.positions_list[3] = (axis[0], axis[1] - 2)
                    else:
                        flag = True


            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[2] = new_pos[2]
                self.state = 1


        elif self.state == 1:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[3]
            new_pos.append((axis[0] + 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0], axis[1] + 2))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[3]
                new_pos.append((axis[0] + 1, axis[1] - 2))
                new_pos.append((axis[0], axis[1] - 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] - 2):
                        self.positions_list[3] = (axis[0], axis[1] - 2)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[2] = new_pos[2]
                self.state = 2

        elif self.state == 2:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[3]
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0] + 1, axis[1]))
            new_pos.append((axis[0] + 2, axis[1]))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[3]
                new_pos.append((axis[0], axis[1] + 1))
                new_pos.append((axis[0] + 1, axis[1] + 2))
                new_pos.append((axis[0] + 2, axis[1] + 2))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] + 2):
                        self.positions_list[3] = (axis[0], axis[1] + 2)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[2] = new_pos[2]
                self.state = 3

        elif self.state == 3:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[3]
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0], axis[1] - 2))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[3]
                new_pos.append((axis[0] - 1, axis[1] + 2))
                new_pos.append((axis[0], axis[1] + 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] + 2):
                        self.positions_list[3] = (axis[0], axis[1] + 2)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[2] = new_pos[2]
                self.state = 0


class JTetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(0 ,4), (1, 4), (1, 5), (1, 6)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'blue'
        self.state = 0


    def rotate(self, grid):
        if self.state == 0:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[1]
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0] + 1, axis[1]))
            new_pos.append((axis[0] + 2, axis[1]))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[1]
                new_pos.append((axis[0] - 1, axis[1] + 1))
                new_pos.append((axis[0], axis[1]))
                new_pos.append((axis[0] + 1, axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0] - 1, axis[1]):
                        self.positions_list[1] = (axis[0] - 1, axis[1])
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[2] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 1

        elif self.state == 1:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[1]
            new_pos.append((axis[0] + 1, axis[1]))
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0], axis[1] - 2))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[1]
                new_pos.append((axis[0] + 1, axis[1] + 2))
                new_pos.append((axis[0], axis[1] + 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] + 2):
                        self.positions_list[1] = (axis[0], axis[1] + 2)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[2] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 2

        elif self.state == 2:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[1]
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0] - 2, axis[1]))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[2] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 3

        elif self.state == 3:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[1]
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0], axis[1] + 2))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[1]
                new_pos.append((axis[0] - 1, axis[1] - 2))
                new_pos.append((axis[0], axis[1] - 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] - 2):
                        self.positions_list[1] = (axis[0], axis[1] - 2)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[2] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 0


class TTetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(0, 4), (1, 3), (1, 4), (1, 5)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'purple'
        self.state = 0

    def rotate(self, grid):
        if self.state == 0:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0] + 1, axis[1]))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 1

        elif self.state == 1:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0] + 1, axis[1]))
            new_pos.append((axis[0], axis[1] - 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[2]
                new_pos.append((axis[0], axis[1] + 2))
                new_pos.append((axis[0] + 1, axis[1] + 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] + 2):
                        self.positions_list[2] = (axis[0], axis[1] + 2)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 2

        elif self.state == 2:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0] + 1, axis[1]))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[2]
                new_pos.append((axis[0] - 2, axis[1]))
                new_pos.append((axis[0] - 1, axis[1] - 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0] - 1, axis[1]):
                        self.positions_list[2] = (axis[0] - 1, axis[1])
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 3

        elif self.state == 3:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[2]
                new_pos.append((axis[0], axis[1] - 2))
                new_pos.append((axis[0] - 1, axis[1] - 1))
                new_pos.append((axis[0], axis[1]))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] - 1):
                        self.positions_list[2] = (axis[0], axis[1] - 1)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 0


class ZTetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(0, 4), (0, 5), (1, 5), (1, 6)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'red'
        self.state = 0

    def rotate(self, grid):
        if self.state == 0:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0] + 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0] - 1, axis[1] + 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 1

        elif self.state == 1:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0] - 1, axis[1] - 1))
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[2]
                new_pos.append((axis[0] - 1, axis[1]))
                new_pos.append((axis[0] - 1, axis[1] + 1))
                new_pos.append((axis[0], axis[1] + 2))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True

                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] + 1):
                        self.positions_list[2] = (axis[0], axis[1] + 1)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 0


class STetronimo(Tetronimo):
    def __init__(self):
        super().__init__()
        self.startPositions_list = [(0, 5), (0, 6), (1, 4), (1, 5)]
        self.positions_list = deepcopy(self.startPositions_list)
        self.color = 'green'
        self.state = 0

    def rotate(self, grid):
        if self.state == 0:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0], axis[1] + 1))
            new_pos.append((axis[0] + 1, axis[1] + 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[2]
                new_pos.append((axis[0] - 1, axis[1] + 1))
                new_pos.append((axis[0], axis[1] + 2))
                new_pos.append((axis[0] + 1, axis[1] + 2))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True


            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 1

        elif self.state == 1:
            flag = False
            new_pos = []
            new_pos.clear()
            axis = self.positions_list[2]
            new_pos.append((axis[0], axis[1] - 1))
            new_pos.append((axis[0] - 1, axis[1]))
            new_pos.append((axis[0] - 1, axis[1] + 1))
            for pos in new_pos:
                if not grid.check_if_move_is_valid(pos[0], pos[1]):
                    flag = True

            if flag:
                flag = False
                new_pos = []
                new_pos.clear()
                axis = self.positions_list[2]
                new_pos.append((axis[0], axis[1]))
                new_pos.append((axis[0] - 1, axis[1] + 1))
                new_pos.append((axis[0] - 1, axis[1] + 2))
                for pos in new_pos:
                    if not grid.check_if_move_is_valid(pos[0], pos[1]):
                        flag = True


                if not flag:
                    if grid.check_if_move_is_valid(axis[0], axis[1] + 1):
                        self.positions_list[2] = (axis[0], axis[1] + 1)
                    else:
                        flag = True

            if not flag:
                self.positions_list[0] = new_pos[0]
                self.positions_list[1] = new_pos[1]
                self.positions_list[3] = new_pos[2]
                self.state = 0

