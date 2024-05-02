import os.path
from tkinter import Toplevel, Label, Button
import pickle


class Scoreboard:
    def __init__(self, root):
        self.root = root
        self.scoreboard = Toplevel(root)
        self.scoreboard.geometry('550x190')
        self.scoreboard.resizable(False, False)
        self.scoreboard.title('Scoreboard')

        default_dice = (0, 0, 0)
        default_guess = (0, 0)
        default_rps = (0, 0, 0)

        if os.path.exists('dice.pkl'):
            with open('dice.pkl', 'rb') as pickle_in:
                dice = pickle.load(pickle_in)
        else:
            dice = default_dice

        if os.path.exists('guess.pkl'):
            with open('guess.pkl', 'rb') as pickle_in:
                guess = pickle.load(pickle_in)
        else:
            guess = default_guess

        if os.path.exists('rps.pkl'):
            with open('rps.pkl', 'rb') as pickle_in:
                rps = pickle.load(pickle_in)
        else:
            rps = default_rps

        self.dice_wins, self.dice_losses, self.dice_draws = dice
        self.guess_wins, self.guess_losses = guess
        self.rps_wins, self.rps_losses, self.rps_draws = rps

        self.dice_label = Label(self.scoreboard, text='Dice game', font=('Arial', 12, 'bold'))
        self.guess_label = Label(self.scoreboard, text='Guess game', font=('Arial', 12, 'bold'))
        self.rps_label = Label(self.scoreboard, text='Rock, Paper, Scissors game', font=('Arial', 12, 'bold'))

        self.wins = Label(self.scoreboard, text='Wins:', font=('Arial', 12))
        self.loses = Label(self.scoreboard, text='Losses:', font=('Arial', 12))
        self.draws = Label(self.scoreboard, text='Draws:', font=('Arial', 12))

        self.dice_score_wins = Label(self.scoreboard, text='0')
        self.dice_score_losses = Label(self.scoreboard, text='0')
        self.dice_score_draws = Label(self.scoreboard, text='0')

        self.guess_score_wins = Label(self.scoreboard, text='0')
        self.guess_score_losses = Label(self.scoreboard, text='0')

        self.rps_score_wins = Label(self.scoreboard, text='0')
        self.rps_score_losses = Label(self.scoreboard, text='0')
        self.rps_score_draws = Label(self.scoreboard, text='0')

        self.dice_score_wins['text'] = f'{self.dice_wins}'
        self.dice_score_losses['text'] = f'{self.dice_losses}'
        self.dice_score_draws['text'] = f'{self.dice_draws}'

        self.guess_score_wins['text'] = f'{self.guess_wins}'
        self.guess_score_losses['text'] = f'{self.guess_losses}'

        self.rps_score_wins['text'] = f'{self.rps_wins}'
        self.rps_score_losses['text'] = f'{self.rps_losses}'
        self.rps_score_draws['text'] = f'{self.rps_draws}'

        self.quitButton = Button(self.scoreboard, text='Close',
                                 width=10, height=2,
                                 font=('Arial', 15), bg="red", bd=5, activebackground='red', command=self.close_window)

        self.dice_label.grid(row=0, column=1, padx=10)
        self.guess_label.grid(row=0, column=2, padx=10)
        self.rps_label.grid(row=0, column=3, padx=10)

        self.dice_score_wins.grid(row=1, column=1, padx=10)
        self.dice_score_losses.grid(row=2, column=1, padx=10)
        self.dice_score_draws.grid(row=3, column=1, padx=10)

        self.guess_score_wins.grid(row=1, column=2, padx=10)
        self.guess_score_losses.grid(row=2, column=2, padx=10)

        self.rps_score_wins.grid(row=1, column=3, padx=10)
        self.rps_score_losses.grid(row=2, column=3, padx=10)
        self.rps_score_draws.grid(row=3, column=3, padx=10)

        self.wins.grid(row=1, column=0, sticky='e', padx=10)
        self.loses.grid(row=2, column=0, sticky='e', padx=10)
        self.draws.grid(row=3, column=0, sticky='e', padx=10)

        self.quitButton.grid(row=4, column=2, pady=10)

    def close_window(self):
        self.scoreboard.destroy()
        self.root.deiconify()
