from tkinter import *
from checkers import CheckersGame, PLAYER_1, PLAYER_2

class CheckersGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Checkers Game")

        self.game = CheckersGame()
        self.game.initialize_board()

        self.board_frame = Frame(self.root)
        self.board_frame.pack()

        self.buttons = [[None for _ in range(self.game.size)] for _ in range(self.game.size)]

        for row in range(self.game.size):
            for col in range(self.game.size):
                button = Button(self.board_frame, width=4, height=2)
                button.grid(row=row, column=col, padx=1, pady=1)
                self.buttons[row][col] = button

        self.update_board_gui()

        for row in range(self.game.size):
            for col in range(self.game.size):
                self.buttons[row][col].config(command=lambda r=row, c=col: self.button_click(r, c))
