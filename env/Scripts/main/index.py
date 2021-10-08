from fighting import *


clear()

while True:
    print("-"*35)
    print(Fore.GREEN + "Choose a hero" + Fore.RESET)
    for i in range(len(hero)):
        print("%s. %s" % (i+1, hero[i].name))
    print("-"*35)
    n = input()
    while type(n) != int:
        try:
            n = int(n)
        except:
            print(Fore.RED + "Enter number!" + Fore.RESET)
            n = input()
            clear()
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
        print(Fore.RED + "Wrong number!" + Fore.RESET)
        input()
        clear()

# Story

while True:
    menu()

    n = input()
    while type(n) != int:
        try:
            n = int(n)
        except:
            menu()
            print(Fore.RED + "\nEnter number!" + Fore.RESET)
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
            print(Fore.GREEN + "Full HP!" + Fore.RESET)
            input()
        if n == 3:
            clear()
            doctor(hero, 10, 10)
            pass
        if n == 4:
            clear()
            fight(hero, choice(monster))
            if hero.hp == 0:
                input()
                clear()
                break
            input()
