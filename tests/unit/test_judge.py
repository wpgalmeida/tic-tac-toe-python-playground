from unittest import TestCase
from tic_tac_toe_python_playground.judge import all_marked_with_the_same_symbol, check_win, draw


class Test(TestCase):
    def test_should_all_marked_with_the_same_symbol_return_true(self):
        fake_list_to_be_test = ["X", "X", "X"]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assert_(result)

    def test_should_not_is_the_same_symbol_without_none_return_false(self):
        fake_list_to_be_test = ["X", "O", "X"]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_not_is_the_same_symbol_with_none_return_false(self):
        fake_list_to_be_test = ["X", None, "X"]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_all_none_return_false(self):
        fake_list_to_be_test = [None, None, None]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_4_same_symbol_return_true(self):
        fake_list_to_be_test = ["X", "X", "X", "X"]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assert_(result)

    def test_should_4_not_is_the_same_symbol_without_none_return_false(self):
        fake_list_to_be_test = ["X", "O", "X", "O"]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)

    def test_should_4_not_is_the_same_symbol_with_none_return_false(self):
        fake_list_to_be_test = ["X", "X", "X", None]
        result = all_marked_with_the_same_symbol(fake_list_to_be_test)
        self.assertFalse(result)


class Test(TestCase):
    def test_check_win_row0(self):
        fake_list_to_be_test = [
            ["X", "X", "X"],
            [None, None, None],
            [None, None, None]
        ]
        result = check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_check_win_row1(self):
        fake_list_to_be_test = [
            [None, None, None],
            ["O", "O", "O"],
            [None, None, None]
        ]
        result = check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_check_win_row2(self):
        fake_list_to_be_test = [
            [None, None, None],
            [None, None, None],
            ["O", "O", "O"]
        ]
        result = check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_check_win_col0(self):
        fake_list_to_be_test = [
            ["O", None, None],
            ["O", None, None],
            ["O", None, None]
        ]
        result = check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_check_win_col1(self):
        fake_list_to_be_test = [
            [None, "O", None],
            [None, "O", None],
            [None, "O", None]
        ]
        result = check_win(fake_list_to_be_test)
        self.assert_(result)

    def test_check_win_col2(self):
        fake_list_to_be_test = [
            [None, None, "O"],
            [None, None, "O"],
            [None, None, "O"]
        ]
        result = check_win(fake_list_to_be_test)
        self.assert_(result)


class Test(TestCase):
    def test_draw_is_true(self):
        fake_list_to_be_test = [
            ["X", "X", "O"],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = draw(fake_list_to_be_test)
        self.assert_(result)

    def test_draw_is_false(self):
        fake_list_to_be_test = [
            ["X", "X", None],
            ["0", "O", "X"],
            ["X", "X", "O"]
        ]
        result = draw(fake_list_to_be_test)
        self.assertFalse(result)
