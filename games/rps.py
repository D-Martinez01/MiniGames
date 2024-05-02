import os.path
import pickle
import random
from tkinter import Toplevel, Button, Label, PhotoImage


class Rps:
    def __init__(self, root):
        self.root = root
        self.rps = Toplevel(root)
        self.rps.geometry('750x830')
        self.rps.resizable(False, False)
        self.rps.title('RPS')

        if os.path.exists('rps.pkl'):
            with open('rps.pkl', 'rb') as pickle_in:
                scoreboard = pickle.load(pickle_in)
                self.wins, self.losses, self.draws = scoreboard
        else:
            self.wins = 0
            self.losses = 0
            self.draws = 0

        self.player_option = None

        self.blank_img = PhotoImage(file='games/images/blank.png')
        self.player_rock = PhotoImage(file='games/images/player_rock.png')
        self.player_paper = PhotoImage(file='games/images/player_paper.png')
        self.player_scissors = PhotoImage(file='games/images/player_scissor.png')

        self.computer_rock = PhotoImage(file='games/images/com_rock.png')
        self.computer_paper = PhotoImage(file='games/images/com_paper.png')
        self.computer_scissors = PhotoImage(file='games/images/com_scissor.png')

        self.image_player = Label(self.rps, image=self.blank_img)
        self.image_computer = Label(self.rps, image=self.blank_img)
        self.label_player = Label(self.rps, text='PLAYER', font=('Arial', 15, 'bold'))
        self.label_computer = Label(self.rps, text='COMPUTER', font=('Arial', 18, 'bold'))
        self.label_status = Label(self.rps, text='', font=('Arial', 20, 'bold', 'italic'))

        self.rock = Button(self.rps, image=self.player_rock, command=self.rock)
        self.paper = Button(self.rps, image=self.player_paper, command=self.paper)
        self.scissors = Button(self.rps, image=self.player_scissors, command=self.scissors)

        self.quit_Button = Button(self.rps, text='Close',
                                  width=10, height=2,
                                  font=('Arial', 15), bg="red", bd=5, activebackground='red', command=self.close_window)

        self.wins_label = Label(self.rps, text=f'Wins: {self.wins}', font=('Arial', 10))
        self.loses_label = Label(self.rps, text=f'Losses: {self.losses}', font=('Arial', 10))
        self.draws_label = Label(self.rps, text=f'Draws: {self.draws}', font=('Arial', 10))

        self.label_player.grid(row=1, column=1)
        self.label_computer.grid(row=1, column=3)
        self.image_player.grid(row=2, column=1, padx=30, pady=20)
        self.image_computer.grid(row=2, column=3, pady=20)
        self.label_status.grid(row=3, column=2)

        self.rock.grid(row=4, column=1, pady=30)
        self.paper.grid(row=4, column=2, pady=30)
        self.scissors.grid(row=4, column=3, pady=30)

        self.quit_Button.grid(row=5, column=2)

        self.wins_label.grid(row=6, column=2)
        self.loses_label.grid(row=7, column=2)
        self.draws_label.grid(row=8, column=2)

    def rock(self):
        self.player_option = 1
        self.image_player.config(image=self.player_rock)
        self.matching()

    def paper(self):
        self.player_option = 2
        self.image_player.config(image=self.player_paper)
        self.matching()

    def scissors(self):
        self.player_option = 3
        self.image_player.config(image=self.player_scissors)
        self.matching()

    def comp_rock(self):
        if self.player_option == 1:
            self.label_status.config(text='Game Tie')
            self.draws += 1
            self.draws_label['text'] = f'Draws: {self.draws}'
        elif self.player_option == 2:
            self.label_status.config(text='You Win')
            self.wins += 1
            self.wins_label['text'] = f'Wins: {self.wins}'
        elif self.player_option == 3:
            self.label_status.config(text='You Lose')
            self.losses += 1
            self.loses_label['text'] = f'Losses: {self.losses}'

    def comp_paper(self):
        if self.player_option == 1:
            self.label_status.config(text='You Lose')
            self.losses += 1
            self.loses_label['text'] = f'Losses: {self.losses}'
        elif self.player_option == 2:
            self.label_status.config(text='Game Tie')
            self.draws += 1
            self.draws_label['text'] = f'Draws: {self.draws}'
        elif self.player_option == 3:
            self.label_status.config(text='You Win')
            self.wins += 1
            self.wins_label['text'] = f'Wins: {self.wins}'

    def comp_scissors(self):
        if self.player_option == 1:
            self.label_status.config(text='You Win')
            self.wins += 1
            self.wins_label['text'] = f'Wins: {self.wins}'
        elif self.player_option == 2:
            self.label_status.config(text='You Lose')
            self.losses += 1
            self.loses_label['text'] = f'Losses: {self.losses}'
        elif self.player_option == 3:
            self.label_status.config(text='Game Tie')
            self.draws += 1
            self.draws_label['text'] = f'Draws: {self.draws}'

    def matching(self):
        computer_option = random.randint(1, 3)
        if computer_option == 1:
            self.image_computer.config(image=self.computer_rock)
            self.comp_rock()
        elif computer_option == 2:
            self.image_computer.config(image=self.computer_paper)
            self.comp_paper()
        elif computer_option == 3:
            self.image_computer.config(image=self.computer_scissors)
            self.comp_scissors()

    def close_window(self):
        scoreboard = (self.wins, self.losses, self.draws)
        with open('rps.pkl', 'wb') as pickle_out:
            pickle.dump(scoreboard, pickle_out)
        self.rps.destroy()
        self.root.deiconify()
