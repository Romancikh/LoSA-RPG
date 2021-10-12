from adventure import *


class Game:
    def __init__(self) -> None:
        self.heroes = [
            Entity("Cleric", 50, 5, race="Hero"),
            Entity("Fighter", 75, 10, race="Hero"),
            Entity("Paladin", 60, 15, race="Hero"),
            Entity("Ranger", 50, 10, dext=15, race="Hero"),
            Entity("Rogue", 50, 10, luck=15, race="Hero"),
            Entity("Mage", 55, 5, race="Hero"),
            Entity("Test", 100, 10, 100, 100, race="Hero")
        ]
        self.hero = None
        self.number_of_actions = 5
        self.adventure = Adventure()

    @print_outline()
    def print_character_list(self) -> None:
        for i in range(len(self.heroes)):
            print("%s. %s" % (i+1, self.heroes[i].name))

    def get_confirm(self, answer: int) -> bool:
        clear()
        self.heroes[answer].print_info()
        confirm = input("\nAre you sure?\n")
        if confirm.lower() in ("yes", "yep", "y", "", " "):
            return True
        return False

    def get_answer(self, number_of_answers: int) -> int:
        answer = input("\nEnter your answer: ")
        while not answer.isnumeric():
            print(red("Enter number!\n"))
            answer = input("Enter your answer: ")
        answer = int(answer) - 1
        if answer in range(number_of_answers):
            return answer
        else:
            print(red("Wrong number!"))
            return self.get_answer(number_of_answers)

    def character_selection(self) -> None:
        while True:
            clear()
            print(green("Choose a hero"))
            self.print_character_list()
            answer = self.get_answer(len(self.heroes))
            if self.get_confirm(answer):
                self.hero = self.heroes[answer]
                break

    @print_outline(True)
    def print_storyline(self) -> None:
        print("You are " + green(self.hero.name) + ".\nEnjoy your life!")

    @print_outline(True)
    def print_actions_list(self) -> None:
        print(green("Choose an action"))
        print("1. STATE")
        print("2. REST")
        print("3. DOCTOR")
        print("4. ADVENTURE")
        print("5. EXIT")

    def action_selection(self) -> None:
        self.print_actions_list()
        answer = self.get_answer(self.number_of_actions) + 1
        self.action(answer)

    def action(self, answer: int) -> None:
        if answer == 1:
            self.hero.print_info()
            input()
        if answer == 2:
            self.rest()
            input()
        if answer == 3:
            self.doctor()
            input()
        if answer == 4:
            self.adventure.start(self.hero)
            input()
        if answer == 5:
            input(cyan("\nThanks for playing!\n"))
            clear()
            exit()
        pass

    @print_outline(True)
    def doctor(self):
        if self.hero.hp == self.hero.hp_max:
            print(green("HP is Full!"))
        else:
            recoverable_value = self.hero.hp_max - self.hero.hp
            payment = recoverable_value // 2 + 1
            confirm = input("Heal %s HP for %s coins?\n" %
                            (recoverable_value, payment))
            if confirm.lower() in ("yes", "yep", "y", ""):
                if self.hero.payment_ability(payment):
                    self.hero.heal(recoverable_value)
                else:
                    print(red("Not enough money!"))
                    print("Need %s more!" % (payment - self.hero.money))

    @print_outline(True)
    def print_recovery_process(self):
        print("HP (%s/%s)" % (self.hero.hp, self.hero.hp_max))
        print("Time remains %ss" % ((self.hero.hp_max - self.hero.hp)*0.5))

    @print_outline(True)
    def rest(self):
        if self.hero.hp == self.hero.hp_max:
            print(green("HP is Full!"))
        else:
            from time import sleep
            while self.hero.hp != self.hero.hp_max:
                self.print_recovery_process()
                self.hero.hp += 1
                sleep(0.5)
            clear()
            print("="*30)
            print(green("HP restored!"))
