from unittest import TestCase
from tic_tac_toe_python_playground.judge import _all_marked_with_the_same_symbol, _check_win, _draw, check_end_game


class Test(TestCase):
    def test_should_all_marked_with_the_same_symbol_return_true(self):
        fake_list_to_be_test = ["X", "X", "X"]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assert_(result)

    def test_should_not_is_the_same_symbol_without_none_return_false(self):
        fake_list_to_be_test = ["X", "O", "X"]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_not_is_the_same_symbol_with_none_return_false(self):
        fake_list_to_be_test = ["X", None, "X"]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_all_none_return_false(self):
        fake_list_to_be_test = [None, None, None]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_4_same_symbol_return_true(self):
        fake_list_to_be_test = ["X", "X", "X", "X"]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assert_(result)

    def test_should_4_not_is_the_same_symbol_without_none_return_false(self):
        fake_list_to_be_test = ["X", "O", "X", "O"]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_4_not_is_the_same_symbol_with_none_return_false(self):
        fake_list_to_be_test = ["X", "X", "X", None]
        result = _all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_check_win_row0(self):
        fake_list_to_be_test = [
            ["X", "X", "X"],
            [None, None, None],
            [None, None, None]
        ]
        result = _check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_should_check_win_row1(self):
        fake_list_to_be_test = [
            [None, None, None],
            ["O", "O", "O"],
            [None, None, None]
        ]
        result = _check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_should_check_win_row2(self):
        fake_list_to_be_test = [
            [None, None, None],
            [None, None, None],
            ["O", "O", "O"]
        ]
        result = _check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_should_check_win_col0(self):
        fake_list_to_be_test = [
            ["O", None, None],
            ["O", None, None],
            ["O", None, None]
        ]
        result = _check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_should_check_win_col1(self):
        fake_list_to_be_test = [
            [None, "O", None],
            [None, "O", None],
            [None, "O", None]
        ]
        result = _check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_should_check_win_col2(self):
        fake_list_to_be_test = [
            [None, None, "O"],
            [None, None, "O"],
            [None, None, "O"]
        ]
        result = _check_win(fake_list_to_be_test)
        self.assert_(result)
    |#TODO: TESTAR SE HOUVE VITORIA NAS DIAGONAIS

    def test_should_inform_draw_is_true_given_all_fields_are_filled(self):
        fake_list_to_be_test = [
            ["X", "X", "O"],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = _draw(fake_list_to_be_test)
        self.assert_(result)
    #TODO: MELHORAR NOMES DOS METODOS DE ACORDO COM A CONVENCAO SHOULD / GIVEN
    def test_should_draw_is_false(self):
        fake_list_to_be_test = [
            ["X", "X", None],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = _draw(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_check_end_game_win_return_true(self):
        fake_list_to_be_test = [
            ["X", "X", "X"],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = check_end_game(fake_list_to_be_test)
        self.assert_(result)

    def test_should_check_end_game_draw_return_true(self):
        fake_list_to_be_test = [
            ["X", "X", "0"],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = check_end_game(fake_list_to_be_test)
        self.assert_(result)

    def test_check_end_game_not_complet_board_return_false(self):
        fake_list_to_be_test = [
            ["X", "X", None],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = check_end_game(fake_list_to_be_test)
        self.assertFalse(result)

    def test_check_end_game_when_board_is_empty_return_false(self):
        fake_list_to_be_test = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        result = check_end_game(fake_list_to_be_test)
        self.assertFalse(result)

