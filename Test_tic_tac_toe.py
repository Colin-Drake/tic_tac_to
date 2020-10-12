import unittest

if __name__ == '__main__':
    unittest.main()

from TicTacToe import check_win_condition
from TicTacToe import check_rows_win
from TicTacToe import check_columns_win
from TicTacToe import check_diagonal_win

NUM_INDICES = ["1", "2", "3"]
CHAR_INDICES = ["a", "b", "c"]


class TestCheckWinCondition(unittest.TestCase):
    def test_row_win(self):
        game_piece = "X"

        current_game_board = {"1": {"a": "O", "b": "O", "c": " "},
                              "2": {"a": "X", "b": "X", "c": "X"},
                              "3": {"a": "X", "b": "O", "c": "O"}}
        result = check_rows_win(current_game_board, game_piece)
        self.assertTrue(result)

    def test_row_no_win(self):
        game_piece = "X"

        current_game_board = {"1": {"a": "X", "b": " ", "c": "X"},
                              "2": {"a": "X", "b": " ", "c": "X"},
                              "3": {"a": "O", "b": " ", "c": "O"}}
        result = check_rows_win(current_game_board, game_piece)
        self.assertFalse(result)

    def test_column_win(self):
        game_piece = "O"

        current_game_board = {"1": {"a": "O", "b": "O", "c": " "},
                              "2": {"a": "X", "b": "O", "c": "X"},
                              "3": {"a": "X", "b": "O", "c": " "}}
        result = check_columns_win(current_game_board, game_piece)
        self.assertTrue(result)

    def test_column_no_win(self):
        game_piece = "X"

        current_game_board = {"1": {"a": "X", "b": " ", "c": "X"},
                              "2": {"a": " ", "b": " ", "c": "X"},
                              "3": {"a": "X", "b": "O", "c": "O"}}
        result = check_columns_win(current_game_board, game_piece)
        self.assertFalse(result)

    def test_diagonal_win_up_to_down(self):
        game_piece = "X"

        current_game_board = {"1": {"a": "X", "b": " ", "c": " "},
                              "2": {"a": " ", "b": "X", "c": " "},
                              "3": {"a": " ", "b": " ", "c": "X"}}
        result = check_diagonal_win(current_game_board, game_piece)
        self.assertTrue(result)


    def test_diagonal_win_down_to_up(self):
        game_piece = "X"

        current_game_board = {"1": {"a": "O", "b": "O", "c": "X"},
                              "2": {"a": "O", "b": "X", "c": "X"},
                              "3": {"a": "X", "b": "O", "c": "O"}}
        result = check_diagonal_win(current_game_board, game_piece)
        self.assertTrue(result)

    def test_Diagonal_no_win(self):
        game_piece = "X"

        current_game_board = {"1": {"a": " ", "b": "O", "c": "X"},
                              "2": {"a": " ", "b": " ", "c": "O"},
                              "3": {"a": " ", "b": "O", "c": "O"}}
        result = check_diagonal_win(current_game_board, game_piece)
        self.assertFalse(result)

    def test_check_win_condition(self):
        game_piece = "X"

        current_game_board = {"1": {"a": "O", "b": "O", "c": "X"},
                              "2": {"a": "O", "b": "X", "c": "X"},
                              "3": {"a": "X", "b": "O", "c": "O"}}
        result = check_win_condition(current_game_board, game_piece)
        self.assertTrue(result)

