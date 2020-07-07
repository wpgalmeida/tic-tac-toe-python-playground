from unittest import TestCase

from tic_tac_toe_python_playground.apps.core.judge import check_end_game


class Test(TestCase):
    def test_should_win_in_row_1(self):
        fake_actual_board_to_be_tested = [["X", "X", "X"], [3, 4, 5], [6, 7, 8]]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_row_2(self):
        fake_actual_board_to_be_tested = [[0, 1, 2], ["X", "X", "X"], [6, 7, 8]]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_row_3(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 5],
            ["X", "X", "X"],
        ]
        self.assertTrue(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_col_1(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 3],
            ["X", 4, 5],
            ["X", 7, 8],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_not_win_in_col_1(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 2],
            ["X", 4, 5],
            [6, 7, 8],
        ]
        self.assertFalse(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_col_2(self):
        fake_actual_board_to_be_tested = [
            [0, "X", 2],
            [3, "X", 5],
            [6, "X", 8],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_not_win_in_col_2(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, "X", 5],
            [6, "X", 8],
        ]
        self.assertFalse(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_col_3(self):
        fake_actual_board_to_be_tested = [
            [0, 1, "X"],
            [3, 4, "X"],
            [6, 7, "X"],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_not_win_in_col_3(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, "X"],
            [6, 7, "X"],
        ]
        self.assertFalse(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_diagonal(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 2],
            [3, "X", 5],
            [6, 7, "X"],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_not_win_in_diagonal(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 2],
            [3, 4, 5],
            [6, 7, "X"],
        ]
        self.assertFalse(check_end_game(fake_actual_board_to_be_tested))

    def test_should_win_in_reverse_diagonal(self):
        fake_actual_board_to_be_tested = [
            [0, 1, "X"],
            [3, "X", 5],
            ["X", 7, 8],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_not_win_in_reverse_diagonal(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, "X", 5],
            ["X", 7, 8],
        ]
        self.assertFalse(check_end_game(fake_actual_board_to_be_tested))

    def test_should_end_game_for_draw(self):
        fake_actual_board_to_be_tested = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))

    def test_should_not_end_game(self):
        fake_actual_board_to_be_tested = [
            ["X", "O", 2],
            ["O", "X", "O"],
            ["O", "X", "O"],
        ]
        self.assertFalse(check_end_game(fake_actual_board_to_be_tested))
