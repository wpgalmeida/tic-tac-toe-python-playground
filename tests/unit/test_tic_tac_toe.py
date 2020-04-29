from unittest import TestCase
from tic_tac_toe_python_playground.tic_tac_toe import create_board, BoardDoesNotHaveTheMaximumConfiguration, \
    BoardDoesNotHaveTheMinimalConfiguration, make_move, check_end_game, CellAlreadyWasPlayedPlayAgain, CellIsNotValid


class Test(TestCase):
    # Build
    def test_should_can_not_create_board_less_than_size_3(self):
        create_board(1)
        self.assertRaises(BoardDoesNotHaveTheMinimalConfiguration, create_board, 2)


    def test_should_number_of_rows_same_the_number_of_cols(self):
        board = create_board()
        number_rows = len(board)
        for row in board:
            number_cols = len(row)
            self.assertEquals(number_cols, number_rows)


    def test_should_can_not_create_board_greather_than_size_10(self):
        create_board(10)
        self.assertRaises(BoardDoesNotHaveTheMaximumConfiguration, create_board, 10)


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

    # Dealer
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

    #Jugde
    def test_should_win_in_row_1(self):
        fake_actual_board_to_be_tested = [
            ["X", "X", "X"],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))


    def test_should_win_in_row_2(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            ["X", "X", "X"],
            [6, 7, 8]
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))


    def test_should_win_in_row_3(self):
        fake_actual_board_to_be_tested = [
            [0, 1, 2],
            [3, 4, 5],
            ["X", "X", "X"],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))


    def test_should_win_in_col_1(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 3],
            ["X", 4, 5],
            ["X", 7, 8],
        ]
        self.assert_(check_end_game(fake_actual_board_to_be_tested))


    def test_should_not_win_in_col_1(self):
        fake_actual_board_to_be_tested = [
            ["X", 1, 3],
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