from entity import *
from json import *
from datetime import datetime


class Save:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.data = {
            "name": None,
            "hp": None,
            "money": None,
            "bag": [],
            "equipment": []
        }

    def make_save(self, hero: Entity) -> None:
        self.data["name"] = hero.name
        self.data["hp"] = hero.hp
        self.data["money"] = hero.money
        for i in hero.inventory.bag:
            if i != None:
                self.data["bag"].append(i.name)
            else:
                self.data["bag"].append(i)
        for i in hero.inventory.equipment:
            if i != None:
                self.data["equipment"].append(i.name)
            else:
                self.data["equipment"].append(i)
        with open(self.file_name + "/hero.json", "w") as save:
            dump(self.data, save, indent=4)

    def load_bag(self, hero: Entity) -> None:
        for i in range(len(self.data["bag"])):
            if self.data["bag"][i] != None:
                item = hero.inventory.get_item_from_list_by_name(
                    self.data["bag"][i])
                hero.inventory.bag[i] = item
            else:
                hero.inventory.bag[i] = None

    def load_equipment(self, hero: Entity) -> None:
        for i in range(len(self.data["equipment"])):
            if self.data["equipment"][i] != None:
                item = hero.inventory.get_item_from_list_by_name(
                    self.data["equipment"][i])
                hero.inventory.equipment[i] = item
            else:
                hero.inventory.equipment[i] = None

    def load_save(self, heroes: list) -> Entity:
        from copy import deepcopy
        with open(self.file_name + "/hero.json", "r") as save:
            self.data = load(save)
        for i in heroes:
            if i.name == self.data["name"]:
                hero = deepcopy(i)
        hero.hp = self.data["hp"]
        hero.money = self.data["money"]
        self.load_bag(hero)
        self.load_equipment(hero)
        return hero

    def open_save(self, dir_name: str) -> None:
        self.file_name = "saves/" + dir_name
        with open(self.file_name + "/hero.json", "r") as save:
            self.data = load(save)


class SavesRepository:
    def __init__(self) -> None:
        self.saves = []

    def read_save(self, dir_name: str) -> None:
        save = Save("saves/" + dir_name)
        save.open_save(dir_name)
        self.saves.append(save)

    def add_save(self, hero) -> None:
        from os import mkdir
        current_time = datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
        mkdir("saves/" + hero.name + " " + current_time)
        save = Save("saves/" + hero.name + " " + current_time)
        save.make_save(hero)
        self.saves.append(save)
        input(yellow("Save made!"))

    def get_save(self, save_id: int) -> Save:
        return self.saves[save_id]

    def get_save_id(self, save) -> int:
        for i in range(len(self.saves)):
            if self.saves[i] == save:
                return i

    def delete_save(self, save_id: int) -> None:
        from os import remove, rmdir
        remove(self.saves[save_id].file_name + "/hero.json")
        rmdir(self.saves[save_id].file_name)
        self.saves.pop(save_id)
        input(blue("Save deleted"))

    @print_outline()
    def print_saves_list(self) -> None:
        for i in range(len(self.saves)):
            print("%s. %s" % (i + 1, self.saves[i].file_name[11:]))
        print("\n%s. exit" % (len(self.saves) + 1))

    def autosave(self, hero) -> None:
        from os import mkdir, listdir
        if "autosave" in listdir("saves/"):
            save = Save("saves/autosave")
            save.make_save(hero)
        else:
            mkdir("saves/autosave")
            save = Save("saves/autosave")
            save.make_save(hero)
            self.read_save("autosave")

    def print_save_info(self, save, heroes: list) -> None:
        save.load_save(heroes).print_info()
        print(green(save.file_name[11:]) + "\n")
