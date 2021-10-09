class Entity:
    def __init__(self, name, hp, dmg, dext=1, luck=1, race="Monster"):
        self.race = race
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.dmg = dmg
        self.dext = dext
        self.luck = luck
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
        output += "Dexterity: " + str(self.dext) + "\n"
        output += "Luck: " + str(self.luck) + "\n"
        if self.race == "Monster":
            output += "Reward: " + str(self.money)
        else:
            output += "Money: " + str(self.money)
        return output

    def __repr__(self):
        return "%s (%s/%s)" % (self.name, self.hp, self.hp_max)


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
    Entity("Ranger", 50, 10, dext=15, race="Hero"),
    Entity("Rogue", 50, 10, luck=15, race="Hero"),
    Entity("Mage", 55, 5, race="Hero")
]
