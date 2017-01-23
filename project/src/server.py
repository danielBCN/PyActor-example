'''
Usage example of the PyActor library versioning a insult server.
Author: Daniel Barcelona Pons <daniel.barcelona@urv.cat>
'''
from random import randint

from pyactor.context import set_context, create_host, sleep, shutdown


class Echo(object):
    _tell = ['echo']
    _ask = []

    def echo(self, msg, sender):
        print sender.get_name(), ':', msg


class Bot(object):
    _tell = ['set_echo', 'send_message']
    _ask = ['get_name']
    _ref = ['set_echo']

    def __init__(self):
        self.responses = ['stupid', 'silly', 'dumb', 'get lost',
                          '...', 'said something?']

    def set_echo(self, echo):
        self.echo = echo

    def get_name(self):
        return self.id

    def send_message(self, message):
        message = None
        self.echo.echo(self.responses[randint(0, 5)], self.proxy)


if __name__ == "__main__":
    set_context()
    h = create_host()
    e1 = h.spawn('Echo', Echo)
    bot = h.spawn('Bot', Bot)
    bot.set_echo(e1)

    print "This is a chat with a bot. Send a message:"
    message = raw_input("You: ")
    bot.send_message(message)

    sleep(1)
    shutdown()
