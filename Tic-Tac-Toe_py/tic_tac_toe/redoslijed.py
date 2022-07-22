def potez(igrac1, igrac2,br,matrica,event):
    if (br == 1):
        matrica = igrac1.napravi_potez(matrica,event)
        br = 2
    else:
        matrica = igrac2.napravi_potez(matrica,event)
        br = 1

    return matrica, br

















"""import random

def redoslijed(igrac1, igrac2):                         #funkcija za odabir redoslijeda igranja i biranja znaka
    br = random.randint(1,2)
    if(br == 1):
        print("Bira " + igrac1.name + "!\n")
        z1 = str(igrac1.odabir_znaka())
        if(z1.upper() == "O"):
            z1 = "O"
            z2 = "X"
        else:
            z1 = "X"
            z2 = "O"
    else:
        print("Bira " + igrac2.name + "!\n")
        z2 = str(igrac2.odabir_znaka())
        if (z2.upper() == "O"):
            z1 = "X"
            z2 = "O"
        else:
            z1 = "O"
            z2 = "X"
    print(igrac1.name + " je " + z1 + ", a " + igrac2.name + " je " + z2 + "!\n")
    return br, z1, z2



def potez(igrac1, igrac2,br,matrica):
    if (br == 1):
        print("Na potezu je " + igrac1.name:\n")
        matrica = igrac1.napravi_potez(matrica)
        br = 2
    else:
        print("Na potezu je " + igrac2.name:\n")
        matrica = igrac2.napravi_potez(matrica)
        br = 1

    return matrica, br

"""