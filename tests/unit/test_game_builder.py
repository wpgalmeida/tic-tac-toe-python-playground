from unittest import TestCase
from tic_tac_toe_python_playground.tic_tac_toe import create_board


class Test(TestCase):
    def test_should_board_be_a_list(self):
        result = create_board(3)
        self.assertEquals(type(result), type([]))

    def test_should_no_create_board_less_3(self):
        result = create_board(2)
        expected = "tabuleiro precisa ter 3 ou mais linhas"
        self.assertEquals(result, expected)

    def test_should_no_create_board_greather_15(self):
        result = create_board(16)
        expected = "tabuleiro muito grande escolha um numero menor"
        self.assertEquals(result, expected)
