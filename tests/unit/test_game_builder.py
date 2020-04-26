from unittest import TestCase
from tic_tac_toe_python_playground.tic_tac_toe import create_board


class Test(TestCase):
    def test_should_board_be_a_list(self):
        result = create_board(3)
        self.assertEquals(type(result), type([]))

    def test_should_return_message_error_if_size_board_less_3(self):
        result = create_board(2)
        expected_message = "tabuleiro precisa ter 3 ou mais linhas"
        self.assertEquals(result, expected_message)

    def test_should_return_message_erro_if_size_board_greather_than_15(self):
        result = create_board(16)
        expected_message = "tabuleiro muito grande escolha um numero menor"
        self.assertEquals(result, expected_message)

    def test_should_create_default_board_3x3(self):
        expected_board_to_be_tested = [[None, None, None], [None, None, None], [None, None, None]]
        result = create_board()
        self.assertEquals(expected_board_to_be_tested, result)

    def test_should_create_customize_board_4x4(self):
        expected_board_4x4_to_be_tested = [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]]
        result = create_board(4)
        self.assertEquals(expected_board_4x4_to_be_tested, result)

    def test_should_create_customize_board_10x10(self):
        expected_board_4x4_to_be_tested = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]]

        result = create_board(10)
        self.assertEquals(expected_board_4x4_to_be_tested, result)