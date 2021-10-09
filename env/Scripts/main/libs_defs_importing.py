from os import system
from time import sleep
from random import choice, randint
from copy import deepcopy
from entities import *
from colorful_text import *


def clear():
    system("cls")


def menu():
    clear()
    print("-"*35)
    print(green("Choose an action"))
    print("1. STATE")
    print("2. REST")
    print("3. DOCTOR")
    print("4. ADVENTURE")
    print("0. EXIT")
    print("-"*35)
