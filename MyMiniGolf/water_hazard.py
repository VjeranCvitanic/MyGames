from bunker import Bunker
from random import randint

class Water_hazard(Bunker):
    def __init__(self):
        super().__init__()
        self.color = (0, 102, 255)
        self.radius1 = randint(30, 50)
        self.radius2 = randint(30, 50)