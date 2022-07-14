from tkinter import *
from tkinter import messagebox

def check_if_win(player1, player2):
    if player1.score == 5:
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('Game over', 'Winner is the red player')
        return True
    elif player2.score == 5:
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('Game over', 'Winner is the blue player')
        return True
