# Constants for players
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
KING_1 = 'X'
KING_2 = 'O'

# Constants for board size
BOARD_SIZE = 8

# CheckersGame class
class CheckersGame:
    def __init__(self):
        #self.board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        #self.current_player = PLAYER_1
        self.board = []
        self.current_player = None
        self.opponent_player = None
        self.size = 8

    def game_over(self):
        return len(self.get_possible_moves(self.current_player)) == 0

    def get_valid_moves(self, row, col):
        moves = []
        piece = self.board[row][col]

        # Check if the current cell contains a player's piece
        if piece == self.current_player:
            # Determine the direction based on the player
            if piece == PLAYER_1:
                directions = [(1, -1), (1, 1)]
            else:
                directions = [(-1, -1), (-1, 1)]

            # Check for regular moves (single step forward)
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if self.is_valid_cell(new_row, new_col) and self.board[new_row][new_col] == EMPTY:
                    moves.append(((row, col), (new_row, new_col)))

            # Check for capture moves (jump over opponent's piece)
            for dx, dy in directions:
                opponent_row = row + dx
                opponent_col = col + dy
                target_row = opponent_row + dx
                target_col = opponent_col + dy
                if (
                    self.is_valid_cell(opponent_row, opponent_col)
                    and self.is_valid_cell(target_row, target_col)
                    and self.board[opponent_row][opponent_col] != EMPTY
                    and self.board[opponent_row][opponent_col] != piece
                    and self.board[target_row][target_col] == EMPTY
                ):
                    moves.append(((row, col), (target_row, target_col)))

        return moves
    def is_valid_cell(self, row, col):
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE