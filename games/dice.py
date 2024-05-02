import random
from tkinter import Toplevel, Button, Label, messagebox
import pickle
import os.path


class Dice:
    def __init__(self, root):
        self.root = root
        self.dice = Toplevel(root)
        self.dice.geometry('550x550')
        self.dice.resizable(False, False)
        self.dice.title('Rolling The Dices Game')

        if os.path.exists('dice.pkl'):
            with open('dice.pkl', 'rb') as pickle_in:
                scoreboard = pickle.load(pickle_in)
                self.wins, self.losses, self.draws = scoreboard
        else:
            self.wins = 0
            self.losses = 0
            self.draws = 0

        self.dice_dots = ['\u2680', '\u2681',
                          '\u2682', '\u2683',
                          '\u2684', '\u2685']

        self.play = Button(self.dice, text="Roll!",
                           width=10, height=2,
                           font=("Arial", 20, "bold"), bg="green", bd=5, activebackground='green',
                           command=self.roll_dice)

        self.label = Label(self.dice, text='User gets', font=("Arial", 25))
        self.user = Label(self.dice, text='', font=('Arial', 80))
        self.label2 = Label(self.dice, text='Computer gets', font=('Arial', 25))
        self.computer = Label(self.dice, text='', font=('Arial', 80))

        self.quitButton = Button(self.dice, text='Close',
                                 width=10, height=2,
                                 font=('Arial', 15), bg="red", bd=5, activebackground='red',
                                 command=self.close_window)

        self.wins_label = Label(self.dice, text=f'Wins: {self.wins}', font=('Arial', 18))
        self.loses_label = Label(self.dice, text=f'Losses: {self.losses}', font=('Arial', 18))
        self.draws_label = Label(self.dice, text=f'Draws: {self.draws}', font=('Arial', 18))

        self.play.grid(row=0, column=1, sticky='nsew')
        self.label.grid(row=1, column=0, sticky='e')
        self.user.grid(row=1, column=1, sticky='e')
        self.label2.grid(row=2, column=0, sticky='e')
        self.computer.grid(row=2, column=1, sticky='e')

        self.quitButton.grid(row=3, column=1)

        self.wins_label.grid(row=4, column=1)
        self.loses_label.grid(row=5, column=1)
        self.draws_label.grid(row=6, column=1)

    def roll_dice(self):
        d1 = random.choice(self.dice_dots)
        d2 = random.choice(self.dice_dots)

        cd1 = random.choice(self.dice_dots)
        cd2 = random.choice(self.dice_dots)

        self.user['text'] = f'{d1}{d2}'
        self.computer['text'] = f'{cd1}{cd2}'

        user_total = self.get_number(d1) + self.get_number(d2)
        computer_total = self.get_number(cd1) + self.get_number(cd2)

        if user_total > computer_total:
            self.wins += 1
            self.wins_label['text'] = f'Wins: {self.wins}'
            messagebox.showinfo('Winner', f'You win')
        elif user_total == computer_total:
            self.draws += 1
            self.draws_label['text'] = f'Draws: {self.draws}'
            messagebox.showinfo('Draw', "It's a draw")
        else:
            self.losses += 1
            self.loses_label['text'] = f'Losses: {self.losses}'
            messagebox.showerror('Lose', 'You lose.')

    def get_number(self, x):
        return self.dice_dots.index(x) + 1

    def close_window(self):
        scoreboard = (self.wins, self.losses, self.draws)
        with open('dice.pkl', 'wb') as pickle_out:
            pickle.dump(scoreboard, pickle_out)
        self.dice.destroy()
        self.root.deiconify()
