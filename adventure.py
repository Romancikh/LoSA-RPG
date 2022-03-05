from save_n_load import *


class Difficulty:
    def __init__(self) -> None:
        self.difficulties = ["Easy", "Medium", "Hard", "Very Hard"]
        self.all_enemies = [
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
        self.difficulty_enemies = []
        self.difficulty_level = 0

    @print_outline()
    def print_difficulty_list(self) -> None:
        for i in range(len(self.difficulties)):
            print("%s. %s" % (i + 1, self.difficulties[i]))

    @print_outline()
    def print_short_data(self, answer: int) -> None:
        self.set_difficulty(answer)
        average_value = 0
        for i in self.difficulty_enemies:
            average_value += i.hp
        average_value /= len(self.difficulty_enemies)
        average_value = round(average_value, 1)
        print("Average HP: %s" % (average_value))
        average_value = 0
        for i in self.difficulty_enemies:
            average_value += i.dmg
        average_value /= len(self.difficulty_enemies)
        average_value = round(average_value, 1)
        print("Average DMG: %s" % (average_value))

    def set_difficulty(self, answer: int) -> None:
        self.difficulty_level = answer
        if self.difficulty_level == 0:
            self.difficulty_enemies = self.all_enemies[:4]
        if self.difficulty_level == 1:
            self.difficulty_enemies = self.all_enemies[4:8]
        if self.difficulty_level == 2:
            self.difficulty_enemies = self.all_enemies[8:12]
        if self.difficulty_level == 3:
            self.difficulty_enemies = self.all_enemies[12:16]


class Adventure():
    def __init__(self) -> None:
        self.difficulty = Difficulty()

    def get_answer(self, number_of_answers: int) -> int:
        answer = input("\nEnter your answer: ")
        while not answer.isnumeric():
            print(red("Enter number!\n"))
            answer = input("Enter your answer: ")
        answer = int(answer) - 1
        if answer in range(number_of_answers):
            return answer
        else:
            print(red("Wrong number!\n"))
            return self.get_answer(number_of_answers)

    def get_confirm(self, answer: int) -> bool:
        clear()
        self.difficulty.print_short_data(answer)
        confirm = input("\nAre you sure?\n")
        if confirm.lower() in ("yes", "yep", "y", "", " "):
            return True
        return False

    def difficulty_selection(self, print_avarage: bool = True) -> None:
        while True:
            clear()
            print(green("Choose the difficulty"))
            self.difficulty.print_difficulty_list()
            answer = self.get_answer(len(self.difficulty.difficulties))
            if print_avarage:
                if self.get_confirm(answer):
                    self.difficulty.set_difficulty(answer)
                    clear()
                    break
                else:
                    clear()
            else:
                self.difficulty.set_difficulty(answer)
                clear()
                break

    def start(self, hero: Entity) -> None:
        self.difficulty_selection()
        from random import choice
        from copy import deepcopy
        self.fight(hero, deepcopy(choice(self.difficulty.difficulty_enemies)))

    def fight(self, hero: Entity, enemy: Entity) -> None:
        print("%s VS %s" % (hero.name, enemy.name))
        print("-" * 30)
        while not any([hero.is_dead(), enemy.is_dead()]):
            enemy.taking_damage(hero)
            hero.taking_damage(enemy)
            print()
        if hero.is_dead():
            input(red("Game Over!\n"))
            clear()
            exit()
        else:
            print("Win!")
            hero.get_money(enemy.money)

    def print_enemy_info(self) -> None:
        self.difficulty_selection(False)
        self.print_enemy_list()
        enemies_list = self.difficulty.difficulty_enemies
        answer = self.get_answer(len(enemies_list))
        enemies_list[answer].print_info()

    @print_outline(True)
    def print_enemy_list(self) -> None:
        enemies_list = self.difficulty.difficulty_enemies
        for i in range(len(enemies_list)):
            print("%s. %s" % (i + 1, enemies_list[i].name))
