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
                
    def update_board_gui(self):
        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.board[row][col] == PLAYER_1:
                    self.buttons[row][col].config(text='O', bg='red')
                elif self.game.board[row][col] == PLAYER_2:
                    self.buttons[row][col].config(text='O', bg='blue')
                else:
                    self.buttons[row][col].config(text='', bg='white')
    def button_click(self, start_row, start_col):
        if self.game.current_player == PLAYER_1:
            moves = self.game.get_possible_moves(PLAYER_1)
            move = self.find_move(moves, start_row, start_col, -1, -1)  # Pass -1, -1 as placeholders for end_row and end_col
            if move is None:
                print("Invalid move for Player 1. Try again.")
                return
            self.game.make_move(*move)
        else:
            moves = self.game.get_possible_moves(PLAYER_2)
            print("Player 2 moves:", moves)  # Print out the moves for debugging
            move = self.find_move(moves, start_row, start_col, -1, -1)  # Pass -1, -1 as placeholders for end_row and end_col
            if move is None:
                print("Invalid move for Player 2. Try again.")
                return
            self.game.make_move(*move)

        self.update_board_gui()
        self.game.current_player = PLAYER_2 if self.game.current_player == PLAYER_1 else PLAYER_1

        if self.game.game_over():
            print("Game over!")

    def find_move(self, moves, start_row, start_col, end_row, end_col):
        for move in moves:
            if move[0] == (start_row, start_col) and move[1] == (end_row, end_col):
                return move
        return None

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = CheckersGUI()
    gui.run()

