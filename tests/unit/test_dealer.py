from unittest import TestCase

from tic_tac_toe_python_playground.dealer import make_move
from tic_tac_toe_python_playground.tic_tac_toe import CellAlreadyWasPlayedPlayAgain, CellIsNotValid


class Test(TestCase):
    def test_should_can_not_move_in_a_cell_that_already_played(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 2],
            [3, 4, 6],
            [6, 7, 8]
        ]
        self.assertRaises(CellAlreadyWasPlayedPlayAgain, make_move, fake_actual_board_to_be_tested, "O", 0)

    def test_should_can_not_move_in_a_cell_out_of_range(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 6],
            [6, 7, 8]
        ]
        self.assertRaises(CellIsNotValid, make_move, fake_actual_board_to_be_tested, "O", 9)

    def test_should_moviment_was_done(self):
        board = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        result_expected_board = [
            ["X", 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        actual_board = make_move(board, "X", 0)
        self.assertEquals(actual_board, result_expected_board)

    def test_should_make_move_in_position_4(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 5],
            [5, 7, 8],
        ]
        expected_board_result = [
            [0, 1, 2],
            [3, 'X', 5],
            [5, 7, 8],
        ]
        result_board = make_move(fake_actual_board_to_be_tested, 4, "X")
        self.assertEquals(expected_board_result, result_board)
