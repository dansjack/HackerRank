import unittest
from io import StringIO
from unittest.mock import patch

from interview_prep.arrays import hourglass_sum, minimum_bribes


class TestArrays(unittest.TestCase):
    def test_hourglass_sum(self):
        self.assertEqual(28, hourglass_sum([[-9, -9, -9, 1, 1, 1],
                                            [0, -9, 0, 4, 3, 2],
                                            [-9, -9, -9, 1, 2, 3],
                                            [0, 0, 8, 6, 6, 0],
                                            [0, 0, 0, -2, 0, 0],
                                            [0, 0, 1, 2, 4, 0]]))

        self.assertEqual(19, hourglass_sum([[1, 1, 1, 0, 0, 0],
                                            [0, 1, 0, 0, 0, 0],
                                            [1, 1, 1, 0, 0, 0],
                                            [0, 0, 2, 4, 4, 0],
                                            [0, 0, 0, 2, 0, 0],
                                            [0, 0, 1, 2, 4, 0]]))

        self.assertEqual(-6, hourglass_sum([[-1, -1, 0, -9, -2, -2],
                                            [-2, -1, -6, -8, -2, -5],
                                            [-1, -1, -1, -2, -3, -4],
                                            [-1, -9, -2, -4, -4, -5],
                                            [-7, -3, -3, -2, -9, -9],
                                            [-1, -3, -1, -2, -4, -0]]))

    @patch('sys.stdout', new_callable=StringIO)
    def test_minimum_bribes(self, mock_stdout):
        test_1 = [2, 1, 5, 3, 4] # list representation of final queue
        test_2 = [2, 5, 1, 3, 4]
        test_3 = [1, 2, 5, 3, 7, 8, 6, 4]
        test_4 = [5, 1, 2, 3, 7, 8, 6, 4]
        minimum_bribes(test_1)
        minimum_bribes(test_2)
        minimum_bribes(test_3)
        minimum_bribes(test_4)
        assert mock_stdout.getvalue() == '3\nToo chaotic\n7\nToo chaotic\n'



