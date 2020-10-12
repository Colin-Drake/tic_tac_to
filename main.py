
from TicTacToe import check_win_condition, new_game_board, get_player_input, update_board, print_board, get_game_piece


def run_game():
    player = 1
    instruction_message = "sample instructions"
    victory_message = f"sample victory player {player}"

    win_condition = False
    current_game_board = new_game_board()
    # new game board sample:
    # {'1': {"a": " ", "b": " ", "c": " "},
    #  '2': {"a": " ", "b": " ", "c": " "},
    #  '3': {"a": " ", "b": " ", "c": " "}}

    # game loop: where the game actually begins.
    while win_condition is False:
        game_piece = get_game_piece(player)
        new_move = get_player_input(player)  # -> {"x": "", "y": ""} or None. TODO should return command instead of None
        if new_move is None:
            continue
        else:
            updated_game_board = update_board(current_game_board, new_move, game_piece)
            if updated_game_board is None:
                continue
            current_game_board = updated_game_board

            print_board(current_game_board)
            # switch player for next turn
            win_condition = check_win_condition(current_game_board, game_piece)
            if win_condition is True:
                return input(f"Player {player} wins!\nPlay again? (y,n)").lower()
            if win_condition is False:
                player = player % 2 + 1


play_again = True
while play_again is True:
    if run_game() == "n":
        play_again = False
print("Thanks for playing!")
# TODO take commands in run_game
# if two numbers are picked it should give an input error
# not properly handling spaces
