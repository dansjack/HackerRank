import unittest


from interview_prep.arrays import hourglass_sum


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
