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
        print("Items :", self.itemsDict)

    # If the item matches what the player asked for
    # return that, and pop it from the itemsDict
    # so the room won't have it anymore
    def get_item(self, itemName):

        item = {}

        if itemName in self.itemsDict:
            item[itemName] = self.itemsDict[itemName]
            print("I found ", itemName)
            self.itemsDict.pop(itemName)

        return item

    # Given a room choice, return the next room number
    # TODO refactor this, unneccesary duplicate valid move check
    def get_next_room(self, moveChoice):

        nextRoomNumber = "0"
        validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

        if moveChoice in validMoves:
            nextRoomNumber = self.movesDict[moveChoice]
            print("Yay, new room is :", nextRoomNumber)

        return nextRoomNumber


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
        print("Your inventory is filled with:")
        for item in self.inventory:
            print(item)


# Print a kick butt intro, lol
def printIntro():
    print("Welcome to the mini dungeon, type exit to quit...")


# Print command options
def printHelp():
    print()
    print("You can enter a direction to move, like : n, ne, e, se, s, sw, w, nw")
    print("-- or --")
    print("You can enter a command such as 'get sword'")
    print()



# Print exit game message
def exitGameMessage():
    print("Ok, bye - have a nice day...")
    print()
    print("Hope ya had fun, you filthy animal!")


# Main Function
def main():

    # define some game variables
    rooms = []
    player = Player()
    currentRoom = "1"
    currentRoomIndex = int(currentRoom) - 1
    continueGame = ""
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

    # Open our game json
    with open('cube2.json') as data_file:
        room_data = json.load(data_file)

    # Lets build a room object for each room in the json file
    # and add it to our rooms list.  This will make it easier later.
    #
    # For each roomDetails in the list of rooms
    for roomDetails in room_data["rooms"]:
        currentRoom = Room(roomDetails)
        rooms.append(currentRoom)


    # Game loop
    while continueGame != "exit":

        room = rooms[currentRoomIndex]
        print("************************")
        room.describe_room()
        player.print_inventory()
        print("************************")
        print()

        commandChoice = input("Enter a command (H for help) -->").lower()
        commandList = commandChoice.split()

        if commandChoice in validMoves:
            nextRoomNumber = room.get_next_room(commandChoice)
            if nextRoomNumber != "0":
                currentRoomIndex = int(nextRoomNumber) - 1
                print()
        elif len(commandList) > 1:
            commandVerb = commandList[0]
            commandNoun = commandList[1]

            if commandVerb == "get":
                newItem = room.get_item(commandNoun)
                if len(newItem) > 0:
                    player.add_item(newItem)
                    player.print_inventory()
                else:
                    print(commandNoun, "is not in the room.")

        elif commandChoice.lower() == "exit":
            break

        elif commandChoice.lower() == "h":
            printHelp()
        else:
            print("Sorry, I don't understand -->", commandChoice)

    exitGameMessage()



if __name__ == "__main__":
    main()
