from unittest import TestCase

from tic_tac_toe_python_playground.apps.core.dealer import make_move


class Test(TestCase):
    def test_should_make_move_in_position_4(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 5],
            [5, 7, 8],
        ]
        expected_board_result = [
            [0, 1, 2],
            [3, "X", 5],
            [5, 7, 8],
        ]
        result_board = make_move(fake_actual_board_to_be_tested, 4, "X")
        self.assertEquals(expected_board_result, result_board)
