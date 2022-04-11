import os
from functions import start
from misc import slowprint

os.system("cls")
slowprint("Hello and welcome to my text based game! What is your name?")
name = input(">>> ")
start(name)

# Read this
# https://pythonbasics.org/python-play-sound/