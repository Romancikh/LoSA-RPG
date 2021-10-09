from colorama import Fore, Back, Style, init
from os import system
from time import sleep
from random import choice, randint
from copy import deepcopy
from entities import *
init()


def clear():
    system("cls")


def menu():
    clear()
    print("-"*35)
    print(Fore.GREEN + "Choose an action" + Fore.RESET)
    print("1. STATE")
    print("2. REST")
    print("3. DOCTOR")
    print("4. ADVENTURE")
    print("0. EXIT")
    print("-"*35)
