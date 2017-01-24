'''
Example project test unit.

Author: Daniel Barcelona Pons <daniel.barcelona@urv.cat>
'''
import unittest
import sys

from pyactor.context import set_context, create_host, sleep, shutdown
from src.server import Echo, Bot


class Outs(object):
    lines = ""

    def write(self, line):
        self.lines += line

    def clear(self):
        self.lines = ""


class BasicTest(unittest.TestCase):
    def setUp(self):
        # This is executed before each test.
        set_context()
        self.h = create_host()
        self.e1 = self.h.spawn('Echo', Echo)
        self.bot = self.h.spawn('Bot', Bot)
        self.bot.set_echo(self.e1)
        self.stdo = sys.stdout
        self.out = Outs()
        sys.stdout = self.out

    def tearDown(self):
        # This is executed after each test. Doesn't matter if the test failed
        # or was successful.
        shutdown()
        self.out.clear()
        sys.stdout = self.stdo

    def test_mytest(self):
        # This is the test. You can put as much of them as you want. The name
        # must begin with 'test'.
        self.bot.send_message("hi")
        sleep(.5)
        self.assertEquals("Bot : ...\n", self.out.lines)


if __name__ == '__main__':
    print ('## Run the tests.')
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
