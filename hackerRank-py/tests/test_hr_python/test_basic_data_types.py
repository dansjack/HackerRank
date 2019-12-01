import unittest
from io import StringIO
from unittest.mock import patch

from hr_python.basic_data_types import list_comprehensions, minion_game


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

    @patch('sys.stdout', new_callable=StringIO)
    def test_minion_game(self, mock_stdout):
        """
        Tests the appropriate name and value are returned
        """
        minion_game('BANANA')
        minion_game('BANANANAAAS')
        assert mock_stdout.getvalue() == 'Stuart 12\nDraw\n'
