from libs_defs_importing import *


def fight(h, m):
    character = [h, m]
    print("%s VS %s" % (h.name, m.name))
    print("-"*30)
    while h.hp > 0 and m.hp > 0:
        for i in range(len(character)):
            if randint(0, 1000) / 10 > character[1-i].dext:
                dmg = character[i].dmg
                is_crit = False
                if randint(0, 1000) / 10 <= character[i].luck:
                    dmg = dmg * 3 // 2
                    is_crit = True
                character[1-i].hp -= dmg
                if character[1-i].hp < 0:
                    character[1-i].hp = 0
                if is_crit:
                    print("%s got " % (repr(character[1-i])) +
                          yellow("CRIT ") + "damage %s" % (dmg))
                else:
                    print("%s got damage %s" %
                          (repr(character[1-i]), dmg))

            else:
                print("%s dodged" % (character[1-i].name))
        print()
    if h.hp > 0:
        print("Win!")
        h.money += m.money
        print(blue("Got money: %s" % (m.money)))
    else:
        print(red("Game Over!"))
