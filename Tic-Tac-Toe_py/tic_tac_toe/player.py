#from ispis import ispis
#include<Python.h>



#matrica = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

class player:
    def __init__(self):
        self.znak = " "
        self.name = " "
        self.win = 0


    def napravi_potez(self, matrica, event):
        while True:
            if event == "1":
                if matrica[0][0] == ' ':
                    matrica[0][0] = self.znak
                    return matrica
            elif event == "2":
                if matrica[0][1] == ' ':
                    matrica[0][1] = self.znak
                    return matrica
            elif event == "3":
                if matrica[0][2] == ' ':
                    matrica[0][2] = self.znak
                    return matrica

            elif event == "4":
                if matrica[1][0] == ' ':
                    matrica[1][0] = self.znak
                    return matrica
            elif event == "5":
                if matrica[1][1] == ' ':
                    matrica[1][1] = self.znak
                    return matrica
            elif event == "6":
                if matrica[1][2] == ' ':
                    matrica[1][2] = self.znak
                    return matrica

            elif event == "7":
                if matrica[2][0] == ' ':
                    matrica[2][0] = self.znak
                    return matrica
            elif event == "8":
                if matrica[2][1] == ' ':
                    matrica[2][1] = self.znak
                    return matrica
            elif event == "9":
                if matrica[2][2] == ' ':
                    matrica[2][2] = self.znak
                    return matrica






"""from ispis import ispis
#include<Python.h>



#matrica = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

class player:
    def __init__(self):
        self.znak = " "
        self.name = " "

    def odabir_znaka(self):
        self.znak = input("Zelis li biti o ili x?<\n")
        if(self.znak.upper() != "O" and self.znak.upper() != "X"):
            print("Krivi unos!\n")
            self.odabir_znaka()
        return self.znak


    def napravi_potez(self,matrica):
        while True:
            a = input("Izaberi polje: \n")
            if a == "a1" or a == "A1":
                if matrica[0][0] == ' ':
                    matrica[0][0] = self.znak
                    ispis(matrica)
                    #click(self.znak)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            elif a == "a2" or a == "A2":
                if matrica[0][1] == ' ':
                    matrica[0][1] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            elif a == "a3" or a == "A3":
                if matrica[0][2] == ' ':
                    matrica[0][2] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")

            elif a == "b1" or a == "B1":
                if matrica[1][0] == ' ':
                    matrica[1][0] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            elif a == "b2" or a == "B2":
                if matrica[1][1] == ' ':
                    matrica[1][1] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            elif a == "b3" or a == "B3":
                if matrica[1][2] == ' ':
                    matrica[1][2] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")

            elif a == "c1" or a == "C1":
                if matrica[2][0] == ' ':
                    matrica[2][0] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            elif a == "c2" or a == "C2":
                if matrica[2][1] == ' ':
                    matrica[2][1] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            elif a == "c3" or a == "C3":
                if matrica[2][2] == ' ':
                    matrica[2][2] = self.znak
                    ispis(matrica)
                    return matrica
                else:
                    print("Greska! Biraj ponovo:\n")
            else:
                print("Krivi unos!" + " Unesi ponovo:\n")




"""


