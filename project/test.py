'''
Example project test unit.

Author: Daniel Barcelona Pons <daniel.barcelona@urv.cat>
'''
import unittest

import src.server


class BasicTest(unittest.TestCase):
    def setUp(self):
        # This is executed before each test.
        pass

    def tearDown(self):
        # Thiss is executed after each test. Doesn't matter if the test failed
        # or was successful.
        pass

    def test_mytest(self):
        # This is the test. You can put as much of them as you want. The name
        # must begin with 'test_'.
        pass


if __name__ == '__main__':
    print ('## Run the tests.')
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
