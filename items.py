from output_improvements import *


class Item:
    def __init__(self, name: str, item_type: str = "junk", hp: int = 0,
                 dmg: int = 0, dext: int = 0,
                 luck: int = 0, price: int = 0) -> None:
        self.name = name
        self.item_type = item_type
        self.hp = hp
        self.dmg = dmg
        self.dext = dext
        self.luck = luck
        self.price = price
        if self.price == 0:
            self.price = 1 + hp + 2 * dmg + 3 * (dext + luck)

    @print_outline(True)
    def print_info(self) -> None:
        print("Item Name: %s" % (self.name))
        print("Type: %s" % (self.item_type))
        if self.hp:
            print(green("HP: %s" % (self.hp)))
        if self.dmg:
            print(red("DMG: %s" % (self.dmg)))
        if self.dext:
            print(cyan("Dexterity: %s" % (self.dext)))
        if self.luck:
            print(magenta("Luck: %s" % (self.luck)))
        print(yellow("Price: %s" % (self.price)))


class ItemRepository:
    def __init__(self, max_volume: int) -> None:
        self.bag = []
        self.equipment = [None, None, None, None]
        self.wearable_item_types = ("WEAPON", "BOOTS",
                                    "CHESTPLATE", "PANTS")
        for i in range(max_volume):
            self.bag.append(None)

    def add_item(self, item: Item) -> None:
        if None in self.bag:
            self.bag[self.bag.index(None)] = item
            print(green("%s added!") % (item.name))
        else:
            print(red("The bag is full!"))

    def delete_item(self, item_id: int) -> None:
        self.bag.pop(item_id)
        self.bag.append(None)

    def get_item_from_bag_by_id(self, item_id: int) -> Item:
        return self.bag[item_id]

    def get_item_from_equipment_by_id(self, item_id: int) -> Item:
        return self.equipment[item_id]

    def get_item_from_list_by_name(self, item_name: str) -> Item:
        for i in item_list:
            if i.name == item_name:
                return i

    def get_bag(self) -> list:
        result = []
        for item in self.bag:
            if item:
                result.append(item)
        return result

    @print_outline(False)
    def print_bag_info(self) -> None:
        print(cyan("Bag:"))
        is_empty = True
        for i in range(len(self.bag)):
            if self.bag[i]:
                print("%s. %s - %s" %
                      (i + 1, self.bag[i].name, self.bag[i].item_type + "\n"))
                is_empty = False
            else:
                print("\r", end="")
        if is_empty:
            print("Empty")

    @print_outline(False)
    def print_equipment_info(self) -> None:
        print(blue("Equipment:"))
        for i in range(len(self.equipment)):
            if self.equipment[i]:
                print("%s. %s: %s" %
                      (i + 1, self.wearable_item_types[i],
                       self.equipment[i].name))
            else:
                print("%s. %s: ---" % (i + 1, self.wearable_item_types[i]))


item_list = [
    Item("Sword", "WEAPON", dmg=5),
    Item("Lether Boots", "BOOTS", hp=5, dext=5),
    Item("Lether Jacket", "CHESTPLATE", hp=10),
    Item("Lether Pants", "PANTS", hp=10)
]
