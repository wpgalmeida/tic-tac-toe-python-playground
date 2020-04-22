from unittest import TestCase

from tic_tac_toe_python_playground.tic_tac_toe import create_board
from tic_tac_toe_python_playground.tic_tac_toe import mark_move

class Test(TestCase):
    def test_should_message_from_size_less_than_3(self):
        returnValue = create_board(1)
        self.assertEquals(returnValue, "tabuleiro precisa ter mais do que 3 linhas")

    def test_should_board_be_a_list(self):
        returnValue = create_board()
        self.assertEquals(type(returnValue), type([]))

    def test_should_standard_board_has_3_rows(self):
        number_of_rows = len(create_board())
        self.assertEquals(number_of_rows, 3)

    def test_should_standard_board_has_3_cols(self):
        board = create_board()

        for board_rows in board:
            number_of_cols = len(board_rows)
            self.assertEquals(number_of_cols, 3)

    def test_should_board_is_empty(self):
        board = create_board()

        for board_rows in board:
            for cells in board_rows:
                self.assertEquals(cells, None)


class Test(TestCase):
    def test_should_made_move(self):
        board = create_board()
        symbol_played = "x"
        row_to_played = 0
        col_to_played = 0
        expected_moved = [['x', None, None], [None, None, None], [None, None, None]]

        actual_board = mark_move(board, symbol_played, row_to_played, col_to_played)

        self.assertEquals(actual_board, expected_moved)

