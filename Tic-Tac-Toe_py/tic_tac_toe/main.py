from player import player
from redoslijed import potez
from kraj import igra_gotova
import PySimpleGUI as sg
from tkinter import messagebox
import array as arr
from scoreboard import scoreBoard
import random



win1 = 0
win2 = 0
tie = 0
output = 0
name1 = " "
name2 = " "
flag1 = 0

igrac1 = player()
igrac2 = player()

#igrac1.znak = "x"
#igrac2.znak = "o"

while True:
        br = 0
        matrica = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        temp = 0

        sg.theme("Random")  # invalid input, pa izbaci random theme
        button1 = sg.Button('1', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))
        button2 = sg.Button('2', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))
        button3 = sg.Button('3', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))

        button4 = sg.Button('4', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))
        button5 = sg.Button('5', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))
        button6 = sg.Button('6', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))

        button7 = sg.Button('7', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))
        button8 = sg.Button('8', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))
        button9 = sg.Button('9', bind_return_key=True, enable_events=True, button_color="gray", size=(4, 2))

        if (flag1 == 0):
            flag1 = 1
            rname1 = [sg.Text("Ime prvog igraca: "), sg.InputText(default_text="Vjeran")]
            rname2 = [sg.Text("Ime drugog igraca: "), sg.InputText(default_text="Anton")]

            layout0 = [
                [rname1, rname2],
                [sg.Button("Enter", enable_events=True, button_color="blue", mouseover_colors="yellow")]
            ]

            window0 = sg.Window("Unos imena igraca: ", layout0)
            a, b = window0.read()

            if (a == "Enter"):
                name1 = b[0]
                name2 = b[1]
            elif (a == sg.WIN_CLOSED):
                name1 = "igrac1"
                name2 = "igrac2"

            window0.close()

        igrac1.name = str(name1)
        igrac2.name = str(name2)

        randBr = random.randint(1, 2)
        if (randBr == 1):
            igracIme = igrac1.name
            igrac1.znak = "x"
            igrac2.znak = "o"
        elif randBr == 2:
            igracIme = igrac2.name
            igrac1.znak = "o"
            igrac2.znak = "x"

        layout = [
            [sg.Text("Igraj krizic kruzic!", text_color="White", justification="left")],
            [sg.Text(
                "Rezultat: " + igrac1.name.upper() + "  (" + igrac1.znak + ") : tie : " + igrac2.name.upper() + " (" + igrac2.znak + ")")],
            [sg.Text(
                "                              " + str(igrac1.win) + "    " + str(tie) + "    " + str(igrac2.win))],
            [sg.Text("Prvi igra " + igracIme)],
            [button1, button2, button3],
            [button4, button5, button6],
            [button7, button8, button9],
            [sg.Button("Izlaz", enable_events=True, button_color="blue", mouseover_colors="yellow"),
             sg.Button("Nova igra", enable_events=True, button_color="blue", mouseover_colors="yellow")],
        ]
        layout2 = [[sg.Text("Tie game")], [sg.Button("OK")]]
        layout3 = [[sg.Text("Winner is " + igrac1.name + "!")], [sg.Button("OK")]]
        layout4 = [[sg.Text("Winner is " + igrac2.name + "!")], [sg.Button("OK")]]
        window = sg.Window("Krizic kruzic", layout, margins=(350, 225))
        over = 0
        flag = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0])

        while True:
            if br % 2 == 0:
                sign = "x"
            else:
                sign = "o"
            event, values = window.read()
            if event == "1" and flag[0] == 0:
                if(br == 1):
                    button1.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button1.Update(text=sign, button_color="orange")
                    br = 1
                flag[0] = 1
                potez(igrac1, igrac2, br, matrica, event)

            elif event == "2" and flag[1] == 0:
                if (br == 1):
                    button2.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button2.Update(text=sign, button_color="orange")
                    br = 1
                flag[1] = 1
                potez(igrac1, igrac2, br, matrica, event)

            elif event == "3" and flag[2] == 0:
                if (br == 1):
                    button3.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button3.Update(text=sign, button_color="orange")
                    br = 1
                flag[2] = 1
                potez(igrac1, igrac2, br, matrica, event)


            elif event == "4" and flag[3] == 0:
                if (br == 1):
                    button4.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button4.Update(text=sign, button_color="orange")
                    br = 1
                flag[3] = 1
                potez(igrac1, igrac2, br, matrica, event)

            elif event == "5" and flag[4] == 0:
                if (br == 1):
                    button5.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button5.Update(text=sign, button_color="orange")
                    br = 1
                flag[4] = 1
                potez(igrac1, igrac2, br, matrica, event)

            elif event == "6" and flag[5] == 0:
                if (br == 1):
                    button6.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button6.Update(text=sign, button_color="orange")
                    br = 1
                flag[5] = 1
                potez(igrac1, igrac2, br, matrica, event)


            elif event == "7" and flag[6] == 0:
                if (br == 1):
                    button7.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button7.Update(text=sign, button_color="orange")
                    br = 1
                flag[6] = 1
                potez(igrac1, igrac2, br, matrica, event)

            elif event == "8" and flag[7] == 0:
                if (br == 1):
                    button8.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button8.Update(text=sign, button_color="orange")
                    br = 1
                flag[7] = 1
                potez(igrac1, igrac2, br, matrica, event)

            elif event == "9" and flag[8] == 0:
                if (br == 1):
                    button9.Update(text=sign, button_color="green")
                    br = 2
                else:
                    button9.Update(text=sign, button_color="orange")
                    br = 1
                flag[8] = 1
                potez(igrac1, igrac2, br, matrica, event)

            if igra_gotova(matrica) == 1:
                window2 = sg.Window("Game over", layout2)
                output = 3
                a3,b3 = window2.read()
                if(a3 == "OK"):
                    window2.close()
                over = 1
                break
            elif (str(igra_gotova(matrica)) == "x"):
                window2 = sg.Window("Game over", layout3)
                output = 1
                a1,b1 = window2.read()
                if(a1 == "OK"):
                    window2.close()
                over = 1
                break
            elif(str(igra_gotova(matrica)) == "o"):
                window2 = sg.Window("Game over", layout4)
                output = 2
                a2,b2 = window2.read()
                if(a2 == "OK"):
                    window2.close()
                over = 1
                break
            if event == "Izlaz" or event == sg.WIN_CLOSED:
                window.close()
                box = messagebox.showinfo("Game over", "You successfully exited!")
                temp = 1
                break

            if over == 1:
                break

            if event == "Nova igra":
                window.close()
                output = 0
                igrac1.win = 0
                igrac2.win = 0
                tie = 0
                flag1 = 0
                break



        igrac1.win, igrac2.win, tie = scoreBoard(igrac1.win, igrac2.win, tie, output)
        if over == 1:
            window.close()

        if temp == 1:
            break

















"""from player import player
from redoslijed import redoslijed, potez
from kraj import igra_gotova
#import gui
while True:

    b = input("\nŽeliš igrati 1v1 -> utipkaj: da\n" + "Izlazak iz menia -> utipkaj: izlaz\n")
    if b.upper() == "DA":
        print("Krece igra krizic kruzic!\n")
        matrica = 0
        matrica = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        igrac1 = 0
        igrac2 = 0

        igrac1 = player()
        igrac2 = player()

       name1 = input("Unesi ime igraca1:\n")
       name2 = input("Unesi ime igraca2:\n")
       igrac1.name = name1
       igrac2.name = name2
        

        br, igrac1.znak, igrac2.znak = redoslijed(igrac1, igrac2)


        while igra_gotova(matrica) == 0:
            matrica, br = potez(igrac1, igrac2, br, matrica)

        if(igra_gotova(matrica) == 1):
            print("Nema pobjednika!\n")
        elif(str(igra_gotova(matrica)) == igrac1.znak):
            print("Pobijedio je: " + igrac1.name + "!")
        elif(str(igra_gotova(matrica)) == igrac2.znak):
            print("Pobijedio je: " +  igrac2.name + "!")

    elif b.upper()== "IZLAZ":
        print("Igra gotova!\n")
        break

    else:
        print("Krivi unos: unesi 'da' ili 'izlaz'\n")










"""





