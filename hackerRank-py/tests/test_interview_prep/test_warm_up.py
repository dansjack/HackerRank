import sys
import unittest
from io import StringIO
from unittest.mock import patch

from interview_prep.warm_up import repeated_string


class TestWarmUp(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_repeated_string(self, mock_stdout):
        repeated_string('abcac', 10)
        repeated_string('aba', 10)
        repeated_string('gfcaaaecbg', 547602)
        repeated_string('a', 1000000000000)
        assert mock_stdout.getvalue() == '4\n7\n164280\n1000000000000\n'

