from libs_defs_importing import *


def doctor(h):
    if h.hp == h.hp_max:
        input(Fore.GREEN + "HP is Full!" + Fore.RESET)
    else:
        recoverable_value = h.hp_max // 2
        payment = recoverable_value // 5
        if h.money >= payment:
            confirm = input("Heal %s HP for %s coins?\n" %
                            (recoverable_value, payment))
            if confirm.lower() in ("yes", "yep", "y", ""):
                h.hp += recoverable_value
                if h.hp > h.hp_max:
                    h.hp = h.hp_max
                h.money -= payment
                input(Fore.GREEN + "%s HP restored" %
                      (recoverable_value) + Fore.RESET)
        else:
            print(Fore.RED + "Not enough money!" + Fore.RESET)
            input("Need %s more!" % (payment - h.money))
    clear()


def rest(h):
    while h.hp != h.hp_max:
        print("HP (%s/%s)" % (h.hp, h.hp_max))
        print("Time remains %ss" % ((h.hp_max - h.hp)*0.5))
        h.hp += 1
        sleep(0.5)
        clear()
