import os.path
import pickle
import random
from tkinter import Toplevel, Label, Button, Entry, messagebox

MAX_ATTEMPTS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100


class Guess:
    def __init__(self, root):
        self.root = root
        self.guess = Toplevel(root)
        self.guess.geometry('300x250')
        self.guess.resizable(False, False)
        self.guess.title('Guess')

        if os.path.exists('guess.pkl'):
            with open('guess.pkl', 'rb') as pickle_in:
                scoreboard = pickle.load(pickle_in)
                self.wins, self.losses = scoreboard
        else:
            self.wins = 0
            self.losses = 0

        self.number = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.guesses = 0

        self.guess_number = Label(self.guess,
                                  text=f'Machine is ready,\n You have {MAX_ATTEMPTS} attempts\n '
                                       f'Guess between {MIN_NUMBER} and {MAX_NUMBER}',
                                  font=("Arial", 15))

        self.guess_entry = Entry(self.guess)
        self.check_button = Button(self.guess, text='Check', command=self.guessing_number)

        self.answer = Label(self.guess, text='', font=("Arial", 10))

        self.quit_button = Button(self.guess, text='Close',
                                  width=8, height=1,
                                  font=('Arial', 15),  bd=5, bg='red',
                                  activebackground='red', command=self.close_window)

        self.wins_label = Label(self.guess, text=f'Wins: {self.wins}', font=('Arial', 10))
        self.loses_label = Label(self.guess, text=f'Losses: {self.losses}', font=('Arial', 10))

        self.guess.columnconfigure(0, weight=1)

        self.guess_number.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.guess_entry.grid(row=1, column=0, sticky='n')
        self.check_button.grid(row=2, column=0, sticky='n')
        self.answer.grid(row=3, column=0, columnspan=4)

        self.quit_button.grid(row=5, column=0, columnspan=4)

        self.wins_label.grid(row=6, column=0)
        self.loses_label.grid(row=7, column=0)

    def guessing_number(self):
        try:
            user_input = int(self.guess_entry.get())
            if user_input < MIN_NUMBER or user_input > MAX_NUMBER:
                raise ValueError
        except ValueError:
            messagebox.showerror('Error', f'Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.')
            return
        self.guesses += 1

        if user_input > self.number:
            self.answer['text'] = f'the number you are looking for is less than {user_input}'
        elif user_input == self.number:
            self.answer['text'] = f'you won in {self.guesses} attempts'
            self.wins += 1
            self.wins_label['text'] = f'Wins: {self.wins}'
            self.guess_entry.config(state='disabled')
            self.check_button['text'] = 'Replay'
            self.check_button['command'] = self.replay
        elif user_input < self.number:
            self.answer['text'] = f'the number you are looking for is greater than {user_input}'

        if self.guesses >= MAX_ATTEMPTS:
            self.answer['text'] = f'you did not find the number\n The number was {self.number}'
            self.losses += 1
            self.loses_label['text'] = f'Losses: {self.losses}'
            self.guess_entry.config(state='disabled')
            self.check_button['text'] = 'Replay'
            self.check_button['command'] = self.replay

    def replay(self):
        scoreboard = (self.wins, self.losses)
        with open('guess.pkl', 'wb') as pickle_out:
            pickle.dump(scoreboard, pickle_out)
        self.guess.destroy()
        self.__init__(self.root)

    def close_window(self):
        scoreboard = (self.wins, self.losses)
        with open('guess.pkl', 'wb') as pickle_out:
            pickle.dump(scoreboard, pickle_out)
        self.guess.destroy()
        self.root.deiconify()
