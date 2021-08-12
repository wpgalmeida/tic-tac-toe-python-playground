from unittest import TestCase

from tic_tac_toe_python_playground.apps.core.game_builder import create_board


class Test(TestCase):
    def test_should_board_be_a_list(self):
        result = create_board(3)
        self.assertEquals(type(result), type([]))

    def test_should_create_default_board_3x3(self):
        expected_board_to_be_tested = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        result = create_board()
        self.assertEquals(expected_board_to_be_tested, result)

    def test_should_create_default_board_4x4(self):
        expected_board_to_be_tested = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        result = create_board(4)
        self.assertEquals(expected_board_to_be_tested, result)
