from random import randint
from copy import deepcopy
from settings import *
import matplotlib.pyplot as plt
import numpy as np


class Array:
    def __init__(self, length = 60, min_value = 0, max_value = 100):
        self.length = length
        self.min_value = min_value
        self.max_value = max_value
        self.elements = []
        self.Create_array()

    def Create_array(self):
        for i in range(self.length - 1):
            self.elements.append(randint(self.min_value, self.max_value))

    def swap(self, i, j):
        temp = deepcopy(self.elements[i])
        self.elements[i] = deepcopy(self.elements[j])
        self.elements[j] = temp

    def BubbleSort(self, screen):
        for i in range(self.length - 1):
            for j in range(self.length - i - 2):
                if self.elements[j] > self.elements[j + 1]:
                    self.swap(j, j+1)
                    return j


    def draw(self, screen, z = -1):
        if z != -1:
            for i in range(self.length - 1):
                if i != z:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     pygame.Rect(i * 10, height - self.elements[i], 10, self.elements[i]), 0)
                else:
                    pygame.draw.rect(screen, 'red', pygame.Rect(i * 10, height - self.elements[i], 10, self.elements[i]), 0)
        else:
            for i in range(self.length - 1):
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(i * 10, height - self.elements[i], 10, self.elements[i]), 0)





