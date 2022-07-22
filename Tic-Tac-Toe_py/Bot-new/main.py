from player import player, Bot
from functions import redoslijed, igra_gotova, potez
while True:
    brPoteza = 0
    matrica = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    igrac1 = player()
    bot = Bot()

    b = input("\nŽeliš igrati vs Bot -> utipkaj: da\n" + "Izlazak iz menia -> utipkaj: izlaz\n")

    if b.upper() == "DA":
        print("Krece igra krizic kruzic!\n")
        br, igrac1.znak, bot.znak = redoslijed(igrac1, bot)

        while igra_gotova(matrica) == 0:
            matrica, br = potez(igrac1.znak, bot, br, matrica, brPoteza)
            brPoteza = brPoteza + 1

        if(igra_gotova(matrica) == 1):
            print("Nema pobjednika!\n")
        elif(str(igra_gotova(matrica)) == igrac1.znak):
            print("Pobijedio je: igrac1!")
        elif(str(igra_gotova(matrica)) == bot.znak):
            print("Pobijedio je: bot!")

    elif b.upper()== "IZLAZ":
        print("Igra gotova!\n")
        break

    else:
        print("Krivi unos: unesi 'da' ili 'izlaz'\n")





