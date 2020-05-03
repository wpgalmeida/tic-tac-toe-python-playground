from unittest import TestCase

from tic_tac_toe_python_playground.dealer import make_move, CellAlreadyWasPlayedPlayAgain, CellIsNotValid


class Test(TestCase):
    def test_should_can_not_move_in_a_cell_that_already_played(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 2],
            [3, 4, 6],
            [6, 7, 8]
        ]
        self.assertRaises(CellAlreadyWasPlayedPlayAgain, make_move, fake_actual_board_to_be_tested, 0, "O")

    def test_should_can_not_move_in_a_cell_out_of_range(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 6],
            [6, 7, 8]
        ]
        self.assertRaises(CellIsNotValid, make_move, fake_actual_board_to_be_tested, 9, "O")

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

    def test_should_make_move_in_position_8_when_already_move_in_other_position(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, "X", 5],
            [5, 7, 8],
        ]
        expected_board_result = [
            [0, 1, 2],
            [3, "X", 5],
            [5, 7, "O"],
        ]
        result_board = make_move(fake_actual_board_to_be_tested, 8, "O")
        self.assertEquals(expected_board_result, result_board)
