from fighting import *
from random import choice
from time import sleep
from os import system


def clear():
    system("cls")


clear()
while True:
    print("-"*35)
    print("Choose a hero")
    for i in range(len(hero)):
        print("%s. %s" % (i+1, hero[i].name))
    print("-"*35)
    n = int(input()) - 1
    clear()
    if n in range(len(hero)):
        print("="*30)
        print(hero[n])
        print("="*30)
        confirm = input("\nAre you sure?\n")
        if confirm.lower() in ["yes", "yep", "y", ""]:
            hero = hero[n]
            clear()
            break
        clear()
    else:
        print("Wrong number!")
        input()

# Story

while True:
    clear()
    print("-"*35)
    print("Choose action")
    print("1. STATE")
    print("2. REST")
    print("3. TRADE")
    print("4. ADVENTURE")
    print("0. EXIT")
    print("-"*35)

    n = int(input())
    print()
    if n in range(5):
        if n == 0:
            clear()
            break
        if n == 1:
            clear()
            print("="*30)
            print(hero)
            print("="*30)
            input()
        if n == 2:
            clear()
            pass
        if n == 3:
            clear()
            pass
        if n == 4:
            clear()
            fight(hero, choice(monster))
            if hero.hp == 0:
                input()
                clear()
                break

            input()
