import json
import random
from classData.room import Room
from classData.player import Player
from classData.monster import Monster
from classData.item import Item

roomsList = []
monstersList = []
itemsList = []

# Game initialization
def game_init():

    print()
    printIntro()
    roomCount = len(roomsList)

    # First places items in any room
    for item in itemsList:
        randomRoom = random.randint(0, roomCount-1)
        currentRoom = roomsList[randomRoom]
        currentRoom.place_item(item)
        roomsList[randomRoom] = currentRoom

    # Now places monsters in any room except the start
    for monster in monstersList:
        randomRoom = random.randint(1, roomCount-1)
        currentRoom = roomsList[randomRoom]
        if currentRoom.monster is None:
            currentRoom.place_monster(monster)
            roomsList[randomRoom] = currentRoom


# Print a kick butt intro, lol
def printIntro():
    print("Welcome to the mini dungeon, type exit to quit...")


# Print command options
def printHelp():
    print()
    print("You can enter a direction to move, like : n, ne, e, se, s, sw, w, nw")
    print("-- or --")
    print("You can enter a command such as 'get sword', 'inventory' or 'status'")
    print()



# Print exit game message
def exitGameMessage():
    print("Ok, bye - have a nice day...")
    print()
    print("Hope ya had fun, you filthy animal!")


# Main Function
def main():

    # define some game variables

    player = Player()
    currentRoom = "1"
    currentRoomIndex = int(currentRoom) - 1
    continueGame = ""
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

    # Open our game json
    with open('./gameData/cube2.json') as data_file:
        game_data = json.load(data_file)

    # Lets build a room object for each room in the json file
    # and add it to our rooms list.  This will make it easier later.
    #
    # For each roomDetails in the list of rooms
    for roomDetails in game_data["rooms"]:
        currentRoom = Room(roomDetails)
        roomsList.append(currentRoom)

    # Lets build a monster object for each monster in the json file
    # and add it to our monster list.  This will make it easier later.
    #
    # For each monsterDetails in the list of monsters:
    for monsterDetails in game_data["monsters"]:
        currentMonster = Monster(monsterDetails)
        monstersList.append(currentMonster)

    # Lets build an item object for each item in the json file
    # and add it to our item list.  This will make it easier later.
    #
    # For each itemDetails in the list of items:
    for itemDetails in game_data["items"]:
        currentItem = Item(itemDetails)
        itemsList.append(currentItem)

    game_init()

    # Game loop
    while continueGame != "exit":

        room = roomsList[currentRoomIndex]
        print("************************")
        print()
        room.describe_room()
        if room.monster != None:
            print("There is a monster in the room! Enough talk, have at you!")
            print()
            room.monster.describe_monster()
            print()
        print()
        print("************************")
        print()

        commandChoice = input("Enter a command (H for help) -->").lower()
        commandList = commandChoice.split()

        if commandChoice in validMoves:
            nextRoomNumber = room.get_next_room(commandChoice)
            if nextRoomNumber != "0":
                currentRoomIndex = int(nextRoomNumber) - 1
                print()
            else:
                room.badMoveMessage()
        elif len(commandList) > 1:
            commandVerb = commandList[0]
            targetItem = ""

            # If we have 2 words in the command, it assumes one is a noun and the other is a verb.
            if len(commandList) == 2:
                targetItem = commandList[1]

            if len(commandList) == 3:
                targetItem = commandList[1] + " " + commandList[2]

            if commandVerb == "get":
                newItem = room.get_item(targetItem)
                if newItem is not None:
                    player.add_item(newItem)
                    player.print_inventory()
                else:
                    print(targetItem, "is not in the room.")
            elif commandVerb == "equip":
                player.equip_weapon(targetItem)

        elif commandChoice.lower() == "h":
            printHelp()

        elif commandChoice.lower() == "i":
            player.print_inventory()

        elif commandChoice.lower() == "status":
            player.print_status()

        elif commandChoice.lower() == "exit":
            break

        else:
            print("Sorry, I don't understand -->", commandChoice)

    exitGameMessage()



if __name__ == "__main__":
    main()
