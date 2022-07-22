import random
from functions import ispis, OneToWin, copyMatrix

class player:
    def __init__(self):
        self.znak = " "



class Bot:
    def __init__(self):
        self.znak = " "

    def NotZnak(self):
        if self.znak == "x":
            return "o"
        else:
            return "x"

    def Move(self, matrica, brPoteza):

        if OneToWin(self.znak, matrica) != 0:
            a, b = OneToWin(self.znak, matrica)
        elif OneToWin(self.NotZnak(), matrica) != 0:
            a, b = OneToWin(self.NotZnak(), matrica)
        elif matrica[1][1] == " ":
            a = 1
            b = 1
        elif self.evaluate(matrica) != -1:
            a, b = self.evaluate(matrica)
        else:
            a = random.randint(0, 2)
            b = random.randint(0, 2)
        while True:
            if matrica[a][b] == " ":
                matrica = self.pot(matrica, a, b)
                return matrica
            a = random.randint(0, 2)
            b = random.randint(0, 2)
        return matrica

    def pot(self, matrica, i, j):
        matrica[i][j] = self.znak
        ispis(matrica)
        return matrica


    def evaluate(self, matrica):
        a = 0
        b = 0
        i = 0
        j = 0

        matrica2 = copyMatrix(matrica)

        while a < 3:
            b = 0
            while b < 3:
                matrica2 = copyMatrix(matrica)
                if matrica2[a][b] == " ":
                    matrica2[a][b] = self.znak
                    if OneToWin(self.znak, matrica2) != 0:
                        a, b = OneToWin(self.znak, matrica2)
                    return a, b
                b = b + 1
            a = a + 1
        return -1


