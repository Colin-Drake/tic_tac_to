NUM_INDICES = ["1", "2", "3"]
CHAR_INDICES = ["a", "b", "c"]
WIN_CONDITION = False


def get_player_input(player):  # -> (num, letter) or None. TODO should return command instead of None
    help_message = "sample help"
    input_error_message = "sample input error"

    user_input = input(f"Player {player}, your move: ")
    # cleans up input by removing spaces and commas  TODO: not working
    clean_user_input = (user_input.replace(" ", "")).replace(",", "")
    coords = {"x": "", "y": ""}

    if len(clean_user_input) == 2:
        try:
            coords["y"] = str(int(clean_user_input[1]))
            coords["x"] = clean_user_input[0].lower()
            return coords
        except:
            pass

    elif user_input.lower() == "help":
        print(help_message)
        return None

    else:
        print(input_error_message)
        return None


def print_board(current_game_board):
    print(f"  a  b  c\n"
          f"1 {current_game_board['1']['a']}  {current_game_board['1']['b']}  {current_game_board['1']['c']}\n"
          f"2 {current_game_board['2']['a']}  {current_game_board['2']['b']}  {current_game_board['2']['c']}\n"
          f"3 {current_game_board['3']['a']}  {current_game_board['3']['b']}  {current_game_board['3']['c']}\n")


def new_game_board():
    print("sample new game text")
    return {"1": {"a": " ", "b": " ", "c": " "},
            "2": {"a": " ", "b": " ", "c": " "},
            "3": {"a": " ", "b": " ", "c": " "}}


def get_game_piece(player):
    if player == 1:
        return "X"
    if player == 2:
        return "O"


def update_board(game_board, coords, game_piece):  # -> updated game_board or None if error
    range_error_message = "sample range error"
    space_taken_message = "sample space taken error"

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


def check_rows_win(current_game_board, game_piece):
    for num_index in NUM_INDICES:
        is_row_win = True
        for char_index in CHAR_INDICES:
            if current_game_board[num_index][char_index] != game_piece:
                is_row_win = False
                break
        if is_row_win is True:
            return True

    return False


def check_columns_win(current_game_board, game_piece):
    for char_index in CHAR_INDICES:
        is_row_win = True
        for num_index in NUM_INDICES:
            if current_game_board[num_index][char_index] != game_piece:
                is_row_win = False
                break
        if is_row_win is True:
            return True

    return False


def check_diagonal_win(current_game_board, game_piece):
    is_row_diagonal = True
    for (idx, char_index) in enumerate(CHAR_INDICES):
        num_index = NUM_INDICES[idx]

        if current_game_board[num_index][char_index] != game_piece:
            is_row_diagonal = False
            break
    if is_row_diagonal is True:
        return True

    is_row_diagonal = True
    for (idx, char_index) in enumerate(reversed(CHAR_INDICES)):
        num_index = NUM_INDICES[idx]
        my_coords = [num_index, char_index]

        if current_game_board[num_index][char_index] != game_piece:
            is_row_diagonal = False
            break

    if is_row_diagonal is True:
        return True

    return False


def check_win_condition(current_game_board, game_piece):
    if check_diagonal_win(current_game_board, game_piece) is True:
        return True
    if check_rows_win(current_game_board, game_piece) is True:
        return True
    if check_columns_win(current_game_board, game_piece) is True:
        return True
    return False


