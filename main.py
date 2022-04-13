import os
from functions import start
from misc import slowprint, printcolor

os.system("cls")
printcolor("========================================", "cyan")
printcolor("-----------------WELCOME----------------", "yellow")
printcolor("========================================", "cyan")
slowprint("Hello and welcome to my text based game! What is your name?")
name = input(">>> ")
start(name)