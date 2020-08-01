import json


# ************************
# Room class
# ************************
class Room:

    # Constructor
    def __init__(self, room):
        # print(room)
        self.roomNumber = room.get("id")
        self.description = room.get("description")
        self.movesDict = room.get("moves")
        self.itemsDict = room.get("items")

    # Describe room
    def describe_room(self):
        print("Room number :", self.roomNumber)
        print("Description :", self.description)
        print()
        print("Eligible moves :", self.movesDict)
        print("Items :", self.itemsDict)

    # If the item matches what the player asked for
    # return that, and pop it from the itemsDict
    # so the room won't have it anymore
    def get_item(self, itemName):

        item = {}

        if self.itemsDict[itemName]:
            item[itemName] = self.itemsDict[itemName]
            print("I found ", itemName)
            self.itemsDict.pop(itemName)

        return item

    def get_next_room(self, moveChoice):
        validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

        if moveChoice in validMoves:
            print("Yay, new room is :", self.movesDict[moveChoice])




# ************************
# Player class
# ************************
class Player:

    # Constructor
    def __init__(self):
        self.inventory = []

    # Add an item to the players inventory
    def add_item(self, item):
        self.inventory.append(item)

    # Remove an item from the players inventory
    def drop_item(self, item):
        self.inventory.remove(item)

    # Print players inventory
    def print_inventory(self):
        for item in self.inventory:
            print(item)


def main():
    # define some game variables
    rooms = []
    player = Player()

    # Open our game json
    # room_data is our json string
    with open('cube2.json') as data_file:
        room_data = json.load(data_file)

    # Lets build a room object for each room in the json file
    # and add it to our rooms list.  This will make it easier later.
    #
    # For each roomDetails in the list of rooms
    for roomDetails in room_data["rooms"]:
        currentRoom = Room(roomDetails)
        rooms.append(currentRoom)


    # Test hitting one room
    testRoom = "2"

    # For each room in the rooms list
    for room in rooms:
        if room.roomNumber == testRoom:
            room.describe_room()
            print("****")
            newItem = room.get_item("sword")

            room.describe_room()
            print("Player inventory before")
            player.print_inventory()
            player.add_item(newItem)
            print("Player inventory after")
            player.print_inventory()

            room.get_next_room("s")

    currentRoom = 3
    room = rooms[currentRoom-1]
    room.describe_room()


if __name__ == "__main__":
    main()
