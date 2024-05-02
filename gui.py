from tkinter import *
from tkinter.ttk import Separator
from games.dice import Dice
from games.guess import Guess
from games.rps import Rps
from scoreboard import Scoreboard


class MiniGames:
    def __init__(self, root):
        self.root = root
        self.root.geometry('250x180')
        self.root.resizable(False, False)
        self.root.iconbitmap('gaming.ico')
        self.root.title('MiniGames')

        self.choose_game = Label(root, text='Choose the game!')

        self.seperator = Separator(root, orient='horizontal')

        self.dice = Button(root, text='Dice', command=self.open_dice)
        self.guess_game = Button(root, text='Guess', command=self.open_guess)
        self.rps_game = Button(root, text='Rock, Paper, Scissors', command=self.open_rps)
        self.games_scoreboard = Button(root, text='Scoreboard', command=self.open_scoreboard)

        self.choose_game.grid(row=0, column=1, sticky='ew')
        self.seperator.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.dice.grid(row=2, column=0, columnspan=3, sticky='ew', pady=5)
        self.guess_game.grid(row=3, column=0, columnspan=3, sticky='ew', pady=5)
        self.rps_game.grid(row=4, column=0, columnspan=3, sticky='ew', pady=5)
        self.games_scoreboard.grid(row=5, column=0, columnspan=3, sticky='ew', pady=5)

        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)

    def open_dice(self):
        new_window(Dice, self.root)

    def open_rps(self):
        new_window(Rps, self.root)

    def open_guess(self):
        new_window(Guess, self.root)

    def open_scoreboard(self):
        new_window(Scoreboard, self.root)


def new_window(game_class, root):
    root.withdraw()
    game_class(root)
