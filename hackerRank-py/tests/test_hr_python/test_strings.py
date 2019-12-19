import unittest
from io import StringIO
from unittest.mock import patch

from hr_python.strings import minion_game


class TestStrings(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_minion_game(self, mock_stdout):
        """
        Tests the appropriate name and value are returned
        """
        minion_game('BANANA')
        minion_game('BANANANAAAS')
        assert mock_stdout.getvalue() == 'Stuart 12\nDraw\n'