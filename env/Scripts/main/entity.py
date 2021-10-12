from output_improvements import *


class Entity:
    def __init__(self, name: str, hp_max: int, dmg_default: int,
                 dext: int = 1, luck: int = 1, race: str = "Monster") -> None:
        self.race = race
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.dmg_default = dmg_default
        self.dmg = dmg_default
        self.dext = dext
        self.luck = luck
        self.money = 10
        if self.race == "Monster":
            self.money = self.hp // 2 + self.dmg

    def __str__(self) -> str:
        return "%s (%s/%s)" % (self.name, self.hp, self.hp_max)

    @print_outline(True)
    def print_info(self) -> None:
        output = ""
        print("Race: %s" % (self.race))
        if self.race == "Monster":
            print("Title: %s" % (self.name))
        else:
            print("Name: %s" % (self.name))
        print(green("Health: %s" % (self.hp)))
        print(red("Damage: %s" % (self.dmg)))
        print("Dexterity: %s" % (self.dext))
        print("Luck: %s" % (self.luck))
        if self.race == "Monster":
            print("Reward: %s" % (self.money))
        else:
            print(yellow("Money: %s" % (self.money)))

    def is_dodged(self) -> bool:
        from random import randint
        random_num = randint(0, 1000) / 10
        return self.dext >= random_num

    def is_crit_hit(self) -> bool:
        from random import randint
        random_num = randint(0, 1000) / 10
        return self.luck >= random_num

    def is_dead(self) -> bool:
        return self.hp <= 0

    def taking_damage(self, enemy) -> None:
        if not enemy.is_dead():
            if self.is_dodged():
                if self.is_crit_hit():
                    print(self.name + cyan(" dodged ") +
                          "and dealt " + yellow("CRIT ") + "damage")
                    self.dmg *= 2
                    enemy.taking_damage(self)
                else:
                    print(self.name + cyan(" dodged"))
            else:
                is_crit = False
                if enemy.dmg == 2 * enemy.dmg_default:
                    is_crit = True
                elif enemy.is_crit_hit():
                    is_crit = True
                    enemy.dmg *= 2
                if self.hp < enemy.dmg:
                    self.hp = 0
                else:
                    self.hp -= enemy.dmg
                if is_crit:
                    print("%s got " % (str(self)) +
                          yellow("CRIT ") + "damage %s" % (enemy.dmg))
                    enemy.dmg = enemy.dmg_default
                else:
                    print("%s got damage %s" % (str(self), enemy.dmg))

    def get_money(self, reward) -> None:
        self.money += reward
        print(blue("Got money: %s" % (reward)))

    def payment_ability(self, price: int) -> bool:
        if price <= self.money:
            self.money -= price
            return True
        return False

    def heal(self, recoverable_value: int) -> None:
        self.hp += recoverable_value
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print(green("%s HP restored" % (recoverable_value)))
