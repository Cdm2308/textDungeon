# ************************
# Item class
# ************************


class Item:

    # Constructor
    def __init__(self, item):
        self.name = item.get("name")
        self.description = item.get("description")
        self.attackDamage = item.get("attackDamage")
        self.quantity = item.get("quantity")

    def describe_item(self):
        print(self.name, ":", self.description, "There are", self.quantity, "of them.", "Attack Damage:", self.attackDamage)
        print()