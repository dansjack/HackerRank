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
        # repeated_string('a', 1000000000000)
        assert mock_stdout.getvalue() == '4\n7\n164280\n'



'''
testing print output example
class TestImplementation(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_count_digits(self, mock_stdout):
        count_digits('77150')
        assert mock_stdout.getvalue() == '0 1\n1 1\n2 0\n3 0\n4 0\n5 1\n6 ' \
                                         '0\n7 2\n8 0\n9 0\n'
 '''