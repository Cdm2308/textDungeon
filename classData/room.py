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
        self.itemsList = []
        self.monster = None


    # Describe room
    def describe_room(self):
        print("Description :", self.description)
        print()
        if len(self.itemsList)>0:
            print("You see the following items:")
            for item in self.itemsList:
                print(item.name)

    # If the item matches what the player asked for
    # return that, and pop it from the itemsDict
    # so the room won't have it anymore
    def get_item(self, itemName):

        returnItem = None

        if itemName in self.itemsList:
            print("I found ", itemName)
            returnItem = self.itemsList.pop(itemName)

        return returnItem

    # Places an item in the room
    def place_item(self, item):
        self.itemsList.append(item)

    def place_monster(self, monster):
        self.monster = monster

    # Given a room choice, return the next room number
    # TODO refactor this, unneccesary duplicate valid move check
    def get_next_room(self, moveChoice):

        return self.movesDict[moveChoice]

    # Prints a message if an invalid move is detected
    def badMoveMessage(self):
        print("You can't go that way... Sorry!")
        print()

