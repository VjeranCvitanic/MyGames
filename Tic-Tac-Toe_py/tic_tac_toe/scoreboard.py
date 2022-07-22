def scoreBoard(win1, win2, tie, output):
    if output == 1:
        win1 = win1 + 1
    elif output == 2:
        win2 = win2 + 1
    elif output == 3:
        tie = tie + 1
    else:
        pass
    return win1, win2, tie

































"""import PySimpleGUI as sg
from tkinter import messagebox
import array as arr

sg.theme("DarkAmber")
button1 = sg.Button('1', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))
button2 = sg.Button('2', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))
button3 = sg.Button('3', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))

button4 = sg.Button('4', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))
button5 = sg.Button('5', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))
button6 = sg.Button('6', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))

button7 = sg.Button('7', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))
button8 = sg.Button('8', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))
button9 = sg.Button('9', bind_return_key=True, enable_events=True, button_color="gray", size=(4,2))

layout =[
    [sg.Text("Igraj krizic kruzic!", text_color="White", justification = "left")],
    [button1, button2, button3],
    [button4, button5, button6],
    [button7, button8, button9],
    [sg.Button("Izlaz", enable_events=True, button_color="blue", mouseover_colors="yellow")],
    [sg.Button("Nova igra", enable_events=True, button_color="blue", mouseover_colors="yellow")]
]
window = sg.Window("Krizic kruzic", layout, margins=(350, 225))
br = 0
flag = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0])

while True:
    if br%2==0:
        sign="x"
    else:
        sign = "o"
    event, values = window.read()
    if event == "1" and flag[0] == 0:
        button1.Update(text=sign)
        br = br + 1
        flag[0] = 1

    elif event == "2" and flag[1] == 0:
        button2.Update(text=sign)
        br = br + 1
        flag[1] = 1

    elif event == "3" and flag[2] == 0:
        button3.Update(text=sign)
        br = br + 1
        flag[2] = 1


    elif event == "4" and flag[3] == 0:
        button4.Update(text=sign)
        br = br + 1
        flag[3] = 1

    elif event == "5" and flag[4] == 0:
        button5.Update(text=sign)
        br = br + 1
        flag[4] = 1

    elif event == "6" and flag[5] == 0:
        button6.Update(text=sign)
        br = br + 1
        flag[5] = 1


    elif event == "7" and flag[6] == 0:
        button7.Update(text=sign)
        br = br + 1
        flag[6] = 1

    elif event == "8" and flag[7] == 0:
        button8.Update(text=sign)
        br = br + 1
        flag[7] = 1

    elif event == "9" and flag[8] == 0:
        button9.Update(text=sign)
        br = br + 1
        flag[8] = 1


    if event == "Izlaz" or event == sg.WIN_CLOSED:
        break

window.close()
box = messagebox.showinfo("Game over", "You successfully exited!")"""