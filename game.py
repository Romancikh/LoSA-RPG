from adventure import *


class Game:
    def __init__(self) -> None:
        self.heroes = [
            Entity("Cleric", 50, 5, 5, 5, "Hero"),
            Entity("Fighter", 75, 10, 5, 5, "Hero"),
            Entity("Paladin", 60, 15, 5, 5, "Hero"),
            Entity("Ranger", 50, 10, 15, 5, "Hero"),
            Entity("Rogue", 50, 10, 5, 15, "Hero"),
            Entity("Mage", 55, 5, 5, 5, "Hero"),
            Entity("Test", 100, 10, 100, 100, "Hero")
        ]
        self.hero = None
        self.actions = ["STATE", "BACKPACK", "BESTIARY", "REST", "DOCTOR",
                        "TRADER", "ADVENTURE", "LOAD", "SAVE", "EXIT"]
        self.adventure = Adventure()
        self.saves_list = SavesRepository()

    def read_saves(self) -> None:
        from os import listdir
        saves_dir_names = listdir("saves/")
        for i in saves_dir_names:
            self.saves_list.read_save(i)

    @print_outline()
    def print_character_list(self) -> None:
        for i in range(len(self.heroes)):
            print("%s. %s" % (i + 1, self.heroes[i].name))

    def get_confirm(self) -> bool:
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
            clear()
            self.heroes[answer].print_info()
            if self.get_confirm():
                self.hero = self.heroes[answer]
                self.saves_list.autosave(self.hero)
                break

    def save_action_selection(self) -> str:
        print("\nChoose an action")
        save_action_list = ["Load", "Delete", "Back"]
        for i in range(len(save_action_list)):
            print("%s. %s" % (i + 1, save_action_list[i]))
        answer = self.get_answer(len(save_action_list))
        if answer == 2:
            return save_action_list[answer]
        if self.get_confirm():
            return save_action_list[answer]

    def save_selection(self) -> [str] or [Save, str]:
        while True:
            clear()
            result = []
            print(green("Choose a save"))
            self.saves_list.print_saves_list()
            number_of_saves = len(self.saves_list.saves) + 1
            answer = self.get_answer(number_of_saves)
            if answer == len(self.saves_list.saves):
                return None
            clear()
            save = self.saves_list.get_save(answer)
            self.saves_list.print_save_info(save, self.heroes)
            save_action = self.save_action_selection()
            if save_action == "Load":
                result = [save_action, self.saves_list.get_save(answer)]
                break
            if save_action == "Delete":
                self.saves_list.delete_save(answer)
                result = [save_action]
                break
            if save_action == "Back":
                clear()
                return self.save_selection()
        return result

    @print_outline(True)
    def print_storyline(self) -> None:
        print("You are " + green(self.hero.name) + ".\nEnjoy your life!")

    @print_outline(True)
    def print_actions_list(self) -> None:
        print(green("Choose an action"))
        for i in range(len(self.actions)):
            print("%s. %s" % (i + 1, self.actions[i]))

    def action_selection(self) -> None:
        self.print_actions_list()
        answer = self.get_answer(len(self.actions)) + 1
        self.action(answer)

    def hero_equip_item(self) -> None:
        if any(self.hero.inventory.bag):
            print(green("Choose an item"))
            self.hero.inventory.print_bag_info()
            answer = self.get_answer(len(self.hero.inventory.bag))
            if self.hero.inventory.bag[answer] == None:
                print(red("Wrong number"))
                input()
            elif self.get_confirm():
                self.hero.equip_item(answer)
                return self.inventory_action_selection()
        else:
            print(red("Inventory is Empty!"))
            input()
            return self.inventory_action_selection()

    def hero_unequip_item(self) -> None:
        if any(self.hero.inventory.equipment):
            print(green("Choose an item"))
            self.hero.inventory.print_equipment_info()
            answer = self.get_answer(
                len(self.hero.inventory.equipment))
            if self.hero.inventory.equipment[answer] == None:
                print(red("Can't Unequip Nothing!"))
                input()
            elif self.get_confirm():
                self.hero.unequip_item(answer)
                return self.inventory_action_selection()
        else:
            print(red("Equipment is Empty!"))
            input()
            return self.inventory_action_selection()

    def selected_item_info(self, storage: str) -> None:
        while True:
            clear()
            if storage == "Bag":
                print(green("Choose an item"))
                self.hero.inventory.print_bag_info()
                answer = self.get_answer(len(self.hero.inventory.bag))
                if self.hero.inventory.bag[answer] == None:
                    print(red("Wrong number!"))
                else:
                    item_list[answer].print_info()
                input()
                break
            elif storage == "Equipment":
                print(green("Choose an item"))
                self.hero.inventory.print_equipment_info()
                answer = self.get_answer(
                    len(self.hero.inventory.equipment))
                if self.hero.inventory.equipment[answer] != None:
                    item_list[answer].print_info()
                else:
                    print(red("Can't Show Nothing"))
                input()
                break

    def bag_or_equipment(self) -> str:
        clear()
        print(green("Choose bag"))
        storage = []
        if any(self.hero.inventory.bag):
            storage.append("Bag")
        if any(self.hero.inventory.equipment):
            storage.append("Equipment")
        for i in range(len(storage)):
            print("%s. %s" % (i + 1, storage[i]))
        answer = self.get_answer(len(storage))
        return storage[answer]

    def selected_item_throw_out(self) -> None:
        while True:
            clear()
            print(green("Choose an item"))
            self.hero.inventory.print_bag_info()
            answer = self.get_answer(len(self.hero.inventory.bag))
            if self.hero.inventory.bag[answer] == None:
                print(red("Wrong number!"))
                input()
            else:
                if self.get_confirm():
                    self.hero.inventory.delete_item(answer)
                    print(magenta("Item Throwed Out"))
                    input()
                    break

    def open_inventory_action_selection(self) -> None:
        while True:
            clear()
            self.hero.inventory.print_bag_info()
            self.hero.inventory.print_equipment_info()
            print(green("Choose an action"))
            open_inventory_action_list = ["View Info", "Throw Out", "Back"]
            for i in range(len(open_inventory_action_list)):
                print("%s. %s" % (i + 1, open_inventory_action_list[i]))
            answer = self.get_answer(len(open_inventory_action_list))
            if answer == 2:
                return self.inventory_action_selection()
            elif answer == 0:
                bag = self.hero.inventory.bag
                equipment = self.hero.inventory.equipment
                if any(bag) or any(equipment):
                    storage = self.bag_or_equipment()
                    self.selected_item_info(storage)
                else:
                    print(red("Empty inventory!"))
                    input()
                    return self.open_inventory_action_selection()
            elif answer == 1:
                bag = self.hero.inventory.bag
                if any(bag):
                    self.selected_item_throw_out()
                else:
                    print(red("Empty bag!"))
                    input()
                    return self.open_inventory_action_selection()

    def inventory_action_selection(self) -> None:
        while True:
            clear()
            print(green("Choose an action"))
            item_action_list = ["Open", "Equip", "Unequip", "Back"]
            for i in range(len(item_action_list)):
                print("%s. %s" % (i + 1, item_action_list[i]))
            answer = self.get_answer(len(item_action_list))
            if answer == 0:
                clear()
                return self.open_inventory_action_selection()
            elif answer == 3:
                clear()
                break
            elif answer == 1:
                clear()
                return self.hero_equip_item()
            elif answer == 2:
                clear()
                return self.hero_unequip_item()
            input()

    def action(self, answer: int) -> None:
        if answer == 1:
            self.hero.print_info()
            input()
        if answer == 2:
            self.inventory_action_selection()
        if answer == 3:
            self.adventure.print_enemy_info()
            input()
        if answer == 4:
            self.rest()
            input()
        if answer == 5:
            self.doctor()
            input()
        if answer == 6:
            self.trader()
        if answer == 7:
            self.saves_list.autosave(self.hero)
            self.adventure.start(self.hero)
            input()
        if answer == 8:
            save = self.save_selection()
            if save == None:
                pass
            elif save[0] == "Load":
                self.hero = save[1].load_save(self.heroes)
                input(yellow("Save loaded!"))
        if answer == 9:
            self.saves_list.add_save(self.hero)
        if answer == 10:
            input(cyan("\nThanks for playing!\n"))
            clear()
            exit()
        pass

    @print_outline(True)
    def is_doctor_price_printed(self, recoverable_value: int,
                                payment: int) -> bool:
        if recoverable_value == 0:
            print(green("HP is Full!"))
            return False
        else:
            print()
            print("Heal %s HP for %s coins?\n" % (recoverable_value, payment))
            return True

    def doctor(self) -> None:
        recoverable_value = self.hero.hp_max - self.hero.hp
        payment = recoverable_value // 2 + 1
        if self.is_doctor_price_printed(recoverable_value, payment):
            if self.get_confirm():
                if self.hero.payment_ability(payment):
                    self.hero.heal(recoverable_value)
                else:
                    print(red("Not enough money!"))
                    print("Need %s more!" % (payment - self.hero.money))

    def buy_item(self) -> None:
        clear()
        sell_item_list = item_list
        for i in range(len(sell_item_list)):
            print("%s. %s - %s for %s" %
                  (i + 1, sell_item_list[i].name,
                   sell_item_list[i].item_type, sell_item_list[i].price))
            print()
        answer = self.get_answer(len(sell_item_list))
        payment = sell_item_list[answer].price
        if self.get_confirm():
            if self.hero.payment_ability(payment):
                self.hero.inventory.add_item(sell_item_list[answer])
                input(green("You Bought Item!"))
            else:
                print(red("Not enough money!"))
                input("Need %s more!" % (payment - self.hero.money))

    def sell_item(self) -> None:
        clear()
        sell_item_list = self.hero.inventory.get_bag()
        if len(sell_item_list) < 1:
            input(red("Empty Inventory"))
            return
        for i in range(len(sell_item_list)):
            print("%s. %s - %s for %s" %
                  (i + 1, sell_item_list[i].name,
                   sell_item_list[i].item_type,
                   int(0.9 * sell_item_list[i].price)))
            print()
        answer = self.get_answer(len(sell_item_list))
        payment = int(0.9 * sell_item_list[i].price)
        if self.get_confirm():
            input(green("You Sold Item!"))
            self.hero.money += payment
            self.hero.inventory.delete_item(answer)

    def trader(self) -> None:
        while True:
            clear()
            print(green("Choose an action"))
            trader_action_list = ["Buy", "Sell", "Back"]
            for i in range(len(trader_action_list)):
                print("%s. %s" % (i + 1, trader_action_list[i]))
            answer = self.get_answer(len(trader_action_list))
            if answer == 2:
                break
            elif answer == 0:
                self.buy_item()
            elif answer == 1:
                self.sell_item()

    @print_outline(True)
    def print_recovery_process(self) -> None:
        print("HP (%s/%s)" % (self.hero.hp, self.hero.hp_max))
        print("Time remains %ss" % ((self.hero.hp_max - self.hero.hp) * 0.5))

    @print_outline(True)
    def rest(self) -> None:
        if self.hero.hp == self.hero.hp_max:
            print(green("HP is Full!"))
        else:
            from time import sleep
            while self.hero.hp != self.hero.hp_max:
                self.print_recovery_process()
                self.hero.hp += 1
                sleep(0.5)
            clear()
            print("=" * 30)
            print(green("HP restored!"))
