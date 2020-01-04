#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config.config import *
import socket
import time



def start_bot():
    try:
        bot = Main(config)
        bot.run()
    except KeyboardInterrupt:
        print "Stopping Betting Bot!"
        exit()
    except socket.error:
        print "Detected Socket Error - Restarted Bot For Your Convenience"
        start_bot()

start_bot()

