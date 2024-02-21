import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
print('sys.path={}'.format(sys.path))

import unittest

from opifex.app import *

running_path = os.getcwd()
print('Current Working Path: {}'.format(running_path))


class TestFunctionMain(unittest.TestCase):    # pragma: no cover

    def setUp(self):
        print()
        print('-'*80)

    def test_call_with_no_args_1(self):
        exception_raised = True
        try:
            result = main()
            exception_raised = False
        except:
            exception_raised = True
        self.assertFalse(exception_raised)



if __name__ == '__main__':
    unittest.main()