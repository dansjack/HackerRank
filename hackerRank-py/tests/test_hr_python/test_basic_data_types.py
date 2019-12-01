import unittest

from hr_python.basic_data_types import list_comprehensions


class TestBasicDataTypes(unittest.TestCase):
    def test_list_comprehension(self):
        """
        Tests that the correct arrays are returned given the inputs

        """
        self.assertEqual(
            [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
            list_comprehensions(1, 1, 1, 2)
        )

        self.assertEqual(
            [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1],
             [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2],
             [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2],
             [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1],
             [2, 2, 2]], list_comprehensions(2, 2, 2, 2))