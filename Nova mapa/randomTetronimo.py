from tetrominoes import *
from random import choice

def randomTetronimo():
    return choice([StraightTetronimo(), SquareTetronimo(), LTetronimo(), JTetronimo(), TTetronimo(), ZTetronimo(), STetronimo()])