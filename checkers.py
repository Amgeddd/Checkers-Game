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
    def get_best_move(self, depth):
        best_score = float('-inf')
        best_move = None
        moves = self.get_possible_moves(self.current_player)
        for move in moves:
            start_row, start_col, end_row, end_col = move
            self.make_move(start_row, start_col, end_row, end_col)
            score = self.minimax(depth - 1, False)
            self.undo_move(start_row, start_col, end_row, end_col)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.game_over():
            # Return the evaluation score for the current position
            return self.evaluate()

        if maximizing_player:
            max_score = float("-inf")
            for move in self.get_possible_moves(self.current_player):
                row, col = move[0]
                new_row, new_col = move[1]
                self.make_move(row, col, new_row, new_col)
                score = self.minimax(depth - 1, alpha, beta, False)
                self.undo_move(row, col, new_row, new_col)
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_score
        else:
            min_score = float("inf")
            opponent_player = self.get_opponent_player()
            for move in self.get_possible_moves(opponent_player):
                row, col = move[0]
                new_row, new_col = move[1]
                self.make_move(row, col, new_row, new_col)
                score = self.minimax(depth - 1, alpha, beta, True)
                self.undo_move(row, col, new_row, new_col)
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_score
