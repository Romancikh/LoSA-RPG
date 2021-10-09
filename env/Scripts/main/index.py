from fighting import *
from npc import *

clear()

while True:
    print("-"*35)
    print(green("Choose a hero"))
    for i in range(len(hero)):
        print("%s. %s" % (i+1, hero[i].name))
    print("-"*35)
    n = input()
    while type(n) != int:
        if n.isnumeric():
            n = int(n) - 1
        else:
            print(red("Enter number!"))
            n = input()
            clear()
    clear()
    if n in range(len(hero)):
        print("="*30)
        print(hero[n])
        print("="*30)
        confirm = input("\nAre you sure?\n")
        if confirm.lower() in ("yes", "yep", "y", ""):
            hero = hero[n]
            clear()
            break
        clear()
    else:
        print(red("Wrong number!"))
        input()
        clear()

# Story
input("Once upon a time, there was a brave and handsome "
      + green(f"{hero.name}\n"))

while True:
    menu()
    n = input()
    while type(n) != int:
        if n.isnumeric():
            n = int(n)
        else:
            menu()
            print(red("Enter number!"))
            n = input()
            clear()
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
            rest(hero)
            print(green("Full HP!"))
            input()
        if n == 3:
            clear()
            doctor(hero)
            pass
        if n == 4:
            clear()
            fight(hero, deepcopy(choice(monster)))
            if hero.hp == 0:
                input()
                clear()
                break
            input()
