# ************************
# Player class
# ************************


class Player:

    # Constructor
    def __init__(self):
        self.inventory = []
        self.hp = 125
        self.weapon = None

    # Add an item to the players inventory
    def add_item(self, item):
        print()
        self.inventory.append(item)

    # Remove an item from the players inventory
    def drop_item(self, item):
        self.inventory.remove(item)

    # Equip an item from Player Inventory
    def equip_weapon(self,item):

        for playerItem in self.inventory:
            if playerItem.name.lower() == item:
                self.weapon = playerItem
                print()
                print("You have equipped your", item, "\n")


    # Print players inventory
    def print_inventory(self):
        if len(self.inventory) > 0:
            print()
            print("Your inventory is filled with:\n")

            # self.inventory is list of dictionaries
            for item in self.inventory:
                item.describe_item()
        else:
            print("You aren't carrying anything.")

        print()

    def describe_weapon(self):
        if self.weapon is not None:
            print()

    def print_status(self):
        print()
        print("Your current health is: ", self.hp)
        print("You are currently wielding your", self.weapon.name, "with attack of", self.weapon.attackDamage)
        print()
