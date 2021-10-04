from os import system
from time import sleep
from random import choice


def clear():
    system("cls")


class Entity:
    def __init__(self, name, hp, dmg, race="Monster"):
        self.race = race
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.dmg = dmg
        self.money = 10
        if self.race == "Monster":
            self.money = self.hp // 2 + self.dmg

    def __str__(self):
        output = ""
        output += "Race: " + str(self.race) + "\n"
        if self.race == "Monster":
            output += "Title: " + str(self.name) + "\n"
        else:
            output += "Name: " + str(self.name) + "\n"
        output += "Health: " + str(self.hp) + "\n"
        output += "Damage: " + str(self.dmg) + "\n"
        if self.race == "Monster":
            output += "Reward: " + str(self.money)
        else:
            output += "Money: " + str(self.money)
        return output

    def __repr__(self):
        return "%s (%s/%s)" % (self.name, self.hp, self.hp_max)


def fight(h, m):
    character = [h, m]
    print("%s VS %s" % (h.name, m.name))
    print("-"*30)
    while h.hp > 0 and m.hp > 0:
        for i in range(len(character)):
            character[1-i].hp -= character[i].dmg
            if character[1-i].hp < 0:
                character[1-i].hp = 0
            print("%s got damage %s" %
                  (repr(character[1-i]), character[i].dmg))
        print()
    if h.hp > 0:
        print("Win!")
        h.money += m.money
        print("Got money: %s" % (m.money))
    else:
        print("Game Over!")


def rest(h):
    while h.hp != h.hp_max:
        print("HP (%s/%s)" % (h.hp, h.hp_max))
        print("Time remains %ss"%((h.hp_max - h.hp)*0.5))
        h.hp += 1
        sleep(0.5)
        clear()


monster = [
    Entity("Mushroom Vampire", 19, 10),
    Entity("Pre-election Sofa", 22, 10),
    Entity("Square Mind", 18, 12),
    Entity("Funny Bread", 20, 10),
    Entity("Safe Horse", 30, 10),
    Entity("Parallel Horror", 27, 11),
    Entity("Wise Ruble", 26, 17),
    Entity("Advertising Crucian", 45, 13),
    Entity("Nervous Yogurt", 49, 24),
    Entity("Free Chipset", 46, 20),
    Entity("Market Croupier", 55, 20),
    Entity("Colossal Plugin", 49, 26),
    Entity("Hot Microbe", 81, 35),
    Entity("Petersburg Eyepiece", 85, 37),
    Entity("Collective Moss", 84, 45),
    Entity("Motley Satan", 68, 32)
]
hero = [
    Entity("Cleric", 50, 5, race="Hero"),
    Entity("Fighter", 75, 10, race="Hero"),
    Entity("Paladin", 60, 15, race="Hero"),
    Entity("Ranger", 50, 10, race="Hero"),  # dexterity  10
    Entity("Rogue", 50, 10, race="Hero"),  # luck 10
    Entity("Mage", 55, 5, race="Hero")
]
