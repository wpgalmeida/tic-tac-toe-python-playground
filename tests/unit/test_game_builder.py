from unittest import TestCase

from tic_tac_toe_python_playground.game_builder import create_board, BoardDoesNotHaveTheMinimalConfiguration, \
    BoardDoesNotHaveTheMaximumConfiguration


class Test(TestCase):
    def test_should_can_not_create_board_less_than_size_3(self):
        self.assertRaises(BoardDoesNotHaveTheMinimalConfiguration, create_board, 2)

    def test_should_number_of_rows_same_the_number_of_cols(self):
        board = create_board()
        number_rows = len(board)
        for row in board:
            number_cols = len(row)
            self.assertEquals(number_cols, number_rows)

    def test_should_can_not_create_board_greather_than_size_10(self):
        self.assertRaises(BoardDoesNotHaveTheMaximumConfiguration, create_board, 11)

    def test_should_standard_board_was_create_with_only_indice_numbers(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        returned_board = create_board()
        self.assertEquals(returned_board, fake_actual_board_to_be_tested)

    def test_should_custom_board_5x5_was_create_with_only_indice_numbers(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],

        ]
        returned_board = create_board(5)
        self.assertEquals(returned_board, fake_actual_board_to_be_tested)