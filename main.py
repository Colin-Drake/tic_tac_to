
def get_player_input(player_idx):  # -> (num, letter) or None. TODO should return command instead of None
    help_message = "sample help"
    input_error_message = "sample input error"

    user_input = input(f"Player {player_idx}, your move: ")
    # clean up input by removing spaces and commas
    clean_user_input = (user_input.replace(" ", "")).replace(",", "")
    coords = {"x": "", "y": ""}

    if len(clean_user_input) == 2:
        try:
            coords["y"] = str(int(user_input[1]))
            coords["x"] = user_input[0].lower()
            return coords
        except:
            pass

    elif user_input.lower() == "help":
        print(help_message)
        return None

    else:
        print(input_error_message)
        return None


def new_game_board():  # feels unnecessary
    print("sample new game text")
    return {"1": {"a": " ", "b": " ", "c": " "},
            "2": {"a": " ", "b": " ", "c": " "},
            "3": {"a": " ", "b": " ", "c": " "}}


def update_board(game_board, player_idx, coords):  # -> updated game_board or None if error
    range_error_message = "sample range error"
    space_taken_message = "sample space taken error"
    game_piece = ""
    # determines which piece to place
    if player_idx == 1:
        game_piece = "X"
    elif player_idx == 2:
        game_piece = "O"

    # makes sure given coords are within play space range, then checks if space is already taken
    if int(coords["y"]) in range(1, 4) and coords["x"] in ["a", "b", "c"]:
        if game_board[coords["y"]][coords["x"]] != " ":
            print(space_taken_message)
            return None
        else:  # now that it has passed the checks it will update the board with the new move.
            game_board[coords["y"]][coords["x"]] = game_piece
            return game_board
    else:  # means coords not in range
        print(range_error_message)
        return None


def run_game():
    player_idx = 1
    instruction_message = "sample instructions"
    victory_message = f"sample victory player_idx {player_idx}"

    win_condition = False
    current_game_board = new_game_board()
    # new game board sample:
    # {'1': {"a": " ", "b": " ", "c": " "},
    #  '2': {"a": " ", "b": " ", "c": " "},
    #  '3': {"a": " ", "b": " ", "c": " "}}

    # game loop: where the game actually begins.
    while win_condition is False:
        new_move = get_player_input(player_idx)  # -> {"x": "", "y": ""} or None. TODO should return command instead of None
        if new_move is None:
            continue
        else:
            updated_game_board = update_board(current_game_board, player_idx, new_move)
            if updated_game_board is None:
                continue
            current_game_board = updated_game_board  # I am sure there is a better way to do this.

            # formats and displays board. cleaner way to do this?
            print(f"""
             a b c            
           1 {current_game_board["1"]["a"]} {current_game_board["1"]["b"]} {current_game_board["1"]["c"]}     
           2 {current_game_board["2"]["a"]} {current_game_board["2"]["b"]} {current_game_board["2"]["c"]}
           3 {current_game_board["3"]["a"]} {current_game_board["3"]["b"]} {current_game_board["3"]["c"]}       
           """)
            # switch player_idx for next turn
            if player_idx == 1:
                player_idx = 2
            else:
                player_idx = 1


run_game()
# TODO win condition, take commands in run_game
# if two numbers are picked, should give an input error
# not properly handling spaces
