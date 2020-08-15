# ************************
# Player class
# ************************


class Player:

    # Constructor
    def __init__(self):
        self.inventory = []
        self.hp = 100

    # Add an item to the players inventory
    def add_item(self, item):
        self.inventory.append(item)

    # Remove an item from the players inventory
    def drop_item(self, item):
        self.inventory.remove(item)

    # Print players inventory
    def print_inventory(self):
        if len(self.inventory) > 0:
            print("Your inventory is filled with:")

            # self.inventory is list of dictionaries
            for itemDict in self.inventory:
                for key, value in itemDict.items():
                    print(value, key)
        else:
            print("You aren't carrying anything.")

        print()

    def print_status(self):
        print()
        print("Your current health is: ", self.hp)
        print()
