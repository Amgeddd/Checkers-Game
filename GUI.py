from checkers import CheckersGame, PLAYER_1, PLAYER_2
import random
import GUI
game = CheckersGame()
game.initialize_board()
game.print_board()

while not game.game_over():
    if game.current_player == PLAYER_1:
        depth = 4  # Adjust the depth as per your requirement
        best_move = game.get_best_move(depth)
        if best_move is None:
            print("Player 1 cannot make any moves. Player 2 wins!")
            break
        print("Player 1 moves:", best_move)
        game.make_move(best_move[0], best_move[1], best_move[2], best_move[3])
    else:
        # You can implement your own logic for player 2
        print("Player 2 moves randomly.")
        moves = game.get_possible_moves(PLAYER_2)
        move = random.choice(moves)
        game.make_move(*move)

    game.print_board()
    game.current_player = PLAYER_2 if game.current_player == PLAYER_1 else PLAYER_1

print("Game over!")
