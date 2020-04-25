from unittest import TestCase

from tic_tac_toe_python_playground.tic_tac_toe import robot_move


class Test(TestCase):
    def test_should_make_a_random_robot_moviment_given_configured_board(self):
        board = [[None, None, None], [None, None, None], [None, None, None]]
        movement_made, actual_board = robot_move(board)

        self.assertTrue(movement_made)
        self.assertIsNotNone(actual_board)
