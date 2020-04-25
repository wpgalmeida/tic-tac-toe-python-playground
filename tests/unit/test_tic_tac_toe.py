from random import randrange
from unittest import TestCase, mock

from tic_tac_toe_python_playground.tic_tac_toe import robot_move


class Test(TestCase):
    def test_should_call_mark_move_with_proper_arguments(self):
        fake_board_to_be_tested = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        with mock.patch("tic_tac_toe_python_playground.tic_tac_toe.mark_move") as mocked_object:
            sample = "calopsita"
            mocked_object.return_value = sample

            must_return_from_sample = robot_move(fake_board_to_be_tested)

            self.assertEqual(must_return_from_sample, sample)
            mocked_object.assert_called_once()

            arguments_received = mocked_object.call_args_list[0][0]
            first_argument_received = arguments_received[0]
            second_argument_received = arguments_received[1]
            third_argument_received = arguments_received[2]
            fourth_argument_received = arguments_received[3]

            max_position = len(fake_board_to_be_tested)
            valid_interval = range(0, max_position)

            self.assertEqual(first_argument_received, fake_board_to_be_tested)
            self.assertEqual(second_argument_received, "O")
            self.assertTrue(third_argument_received in valid_interval)
            self.assertTrue(fourth_argument_received in valid_interval)

        # patcher = mock.patch("tic_tac_toe_python_playground.tic_tac_toe.mark_move")
        # mocked_object = patcher.start()
        #
        # # movement_made, actual_board = robot_move(fake_board_to_be_tested)
        # robot_move(fake_board_to_be_tested)
        #
        # patcher.stop()
        #
        # # self.assertTrue(movement_made)
        # # self.assertIsNotNone(actual_board)
        # self.assertIsNotNone(mocked_object)
