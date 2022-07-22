import random

def redoslijed(igrac1, bot):                         #funkcija za odabir redoslijeda igranja i biranja znaka
    br = random.randint(1,2)
    if(br == 1):
        print("Prvi igra igrac1!\n")
        igrac1.znak = "x"
        bot.znak = "o"
    else:
        print("Prvi igra bot!\n")
        bot.znak = "x"
        igrac1.znak = "o"
    return br, igrac1.znak, bot.znak

def potez(znak, bot, br, matrica, brPoteza):
    if (br == 1):
        print("Na potezu je igrac 1:\n")
        matrica = napravi_potez(znak, matrica)
        br = 2
    else:
        print("Na potezu je bot:\n")
        matrica = bot.Move(matrica, brPoteza)
        br = 1

    return matrica, br


def napravi_potez(znak, matrica):
    while True:
        a = input("Izaberi polje: \n")
        if a == "a1" or a == "A1":
            if matrica[0][0] == ' ':
                matrica[0][0] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        elif a == "a2" or a == "A2":
            if matrica[0][1] == ' ':
                matrica[0][1] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        elif a == "a3" or a == "A3":
            if matrica[0][2] == ' ':
                matrica[0][2] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")

        elif a == "b1" or a == "B1":
            if matrica[1][0] == ' ':
                matrica[1][0] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        elif a == "b2" or a == "B2":
            if matrica[1][1] == ' ':
                matrica[1][1] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        elif a == "b3" or a == "B3":
            if matrica[1][2] == ' ':
                matrica[1][2] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")

        elif a == "c1" or a == "C1":
            if matrica[2][0] == ' ':
                matrica[2][0] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        elif a == "c2" or a == "C2":
            if matrica[2][1] == ' ':
                matrica[2][1] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        elif a == "c3" or a == "C3":
            if matrica[2][2] == ' ':
                matrica[2][2] = znak
                ispis(matrica)
                return matrica
            else:
                print("Greska! Biraj ponovo:\n")
        else:
            print("Krivi unos!" + " Unesi ponovo:\n")



def ispis(matrica):
    print("    1   2   3")
    print("  -------------")
    print("A | " + str(matrica[0][0]) + " | " + str(matrica[0][1]) + " | " + str(matrica[0][2]) + " |")
    print("  -------------")
    print("B | " + str(matrica[1][0]) + " | " + str(matrica[1][1]) + " | " + str(matrica[1][2]) + " |")
    print("  -------------")
    print("C | " + str(matrica[2][0]) + " | " + str(matrica[2][1]) + " | " + str(matrica[2][2]) + " |")
    print("  -------------")
    print("\n////////////////////////////////////////////////////////")
    print("////////////////////////////////////////////////////////")
    return 0

def igra_gotova(m):                                                     #provjerava je li igra gotova

    a = 0
    b = 0

    while(a<3):
        if m[a][b] == m[a][b+1] and m[a][b] == m[a][b+2] and m[a][b] != " ":
            return m[a][b]
        a=a+1

    a = 0
    while (b < 3):
        if m[a][b] == m[a+1][b] and m[a][b] == m[a+2][b] and m[a][b] != " ":
            return m[a][b]
        b=b+1

    b = 0

    if m[0][0] == m[1][1] == m[2][2] != " ":
        return m[1][1]

    elif m[0][2] == m[1][1] == m[2][0] != " ":
        return m[1][1]

    elif m[0][0] != " " and  m[0][1] != " " and m[0][2] != " " and  m[1][0] != " " and m[1][1] != " " and  m[1][2] != " " and m[2][0] != " " and  m[2][1] != " " and m[2][2] != " " :
        return 1
    else:
        return 0


def OneToWin(znak, matrica):
    a = 0
    b = 0
    temp = 0
    f = 0
    while a < 3:
        if matrica[a][0] == matrica[a][1] == znak and matrica[a][2] == " " or matrica[a][1] == matrica[a][2] == znak and \
                matrica[a][0] == " " or matrica[a][0] == matrica[a][2] == znak and matrica[a][1] == " ":
            if matrica[a][0] == matrica[a][1]:
                b = 2
            elif matrica[a][0] == matrica[a][2]:
                b = 1
            else:
                b = 0
            temp = a
            f = 1
            break
        a = a + 1

    if f == 1:
        return temp, b

    a = 0
    b = 0
    while b < 3:
        if matrica[0][b] == matrica[1][b] == znak and matrica[2][b] == " " or matrica[0][b] == matrica[2][b] == znak and \
                matrica[1][b] == " " or matrica[1][b] == matrica[2][b] == znak and matrica[0][b] == " ":
            if matrica[0][b] == " ":
                a = 0
            elif matrica[1][b] == " ":
                a = 1
            else:
                a = 2
            temp = b
            f = 1
            break
        b = b + 1

    if f == 1:
        return a, temp

    if matrica[0][0] == matrica[1][1] == znak and matrica[2][2] == " " or matrica[0][0] == matrica[2][2] == znak and \
            matrica[1][1] == " " or matrica[2][2] == matrica[1][1] == znak and matrica[0][0] == " ":
        if matrica[0][0] == " ":
            a = 0
            b = 0
            f = 1
        elif matrica[1][1] == " ":
            a = 1
            b = 1
            f = 1
        else:
            a = 2
            b = 2
            f = 1

    if f == 1:
        return a, b

    if matrica[0][2] == matrica[1][1] == znak and matrica[2][0] == " " or matrica[0][2] == matrica[2][0] == znak and \
            matrica[1][1] == " " or matrica[2][0] == matrica[1][1] == znak and matrica[0][2] == " ":
        if matrica[0][2] == " ":
            a = 0
            b = 2
            f = 1
        elif matrica[1][1] == " ":
            a = 1
            b = 1
            f = 1
        else:
            a = 2
            b = 0
            f = 1

    if f == 1:
        return a, b

    return 0

def copyMatrix(matrica):
    i = 0
    j = 0
    matrica2 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while i < 3:
        j = 0
        while j < 3:
            matrica2[i][j] = matrica[i][j]
            j = j + 1
        i = i + 1
    return matrica2

"""def checkDiagonals(znak, matrica):
    if matrica[0][0] == znak or matrica[2][2] == znak:
        if matrica[0][2] == " ":
            return 0, 2
        elif matrica[2][0] == " ":
            return 2, 0
        elif matrica[0][0] == " ":
            return 0, 0
        elif matrica[2][2] == " ":
            return 2, 2

    if matrica[0][2] == znak or matrica[2][0] == znak:
        if matrica[0][0] == " ":
            return 0, 0
        elif matrica[2][2] == " ":
            return 2, 2
        elif matrica[0][2] == " ":
            return 0, 2
        elif matrica[2][0] == " ":
            return 2, 0

    return -1

"""

