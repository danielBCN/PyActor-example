"""
Usage example of the PyActor library versioning an insult server.
Author: Daniel Barcelona Pons <daniel.barcelona@urv.cat>
"""
import hashlib

from pyactor.context import set_context, create_host, sleep, shutdown


class Echo(object):
    """
    Echo is a simple channel that prints messages on screen.
    """
    _tell = ['echo']
    _ask = []

    def echo(self, msg, sender):
        """
        Print the message and and the sender as in a chat.

        :param str msg: Message sent to be printed.
        :param proxy sender: The actor that sent the message.
            (Bot in this case)
        """
        print sender.get_name(), ':', msg


class Bot(object):
    """
    Bot is an actor that represents a server that 'answers' messages.
    """
    _tell = ['set_echo', 'send_message']
    _ask = ['get_name']
    _ref = ['set_echo']

    def __init__(self):
        self.responses = ['stupid', 'silly', 'dumb', 'get lost',
                          '...', 'said something?']

    def set_echo(self, echo):
        """
        Sets the echo channel for the bot.

        :param echo: The echo actor channel.
        """
        self.echo = echo

    def get_name(self):
        """
        Returns the name of this bot.

        :return: Str. Its name.
        """
        return self.id

    def send_message(self, message):
        """
        Receives a message and answers it by printing through the echo channel.

        :param str. message: The message sent to the bot.
        """
        m = hashlib.md5()
        m.update(message)
        num = int(m.hexdigest()[:1], 16) % 6
        self.echo.echo(self.responses[num], self.proxy)


if __name__ == "__main__":
    set_context()
    h = create_host()
    e1 = h.spawn('Echo', Echo)
    bot = h.spawn('Bot', Bot)
    bot.set_echo(e1)

    print "This is a chat with a bot. Send a message:"
    message = raw_input("You : ")
    bot.send_message(message)

    sleep(1)
    shutdown()
