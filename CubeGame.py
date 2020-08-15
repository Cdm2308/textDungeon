import json
from classData.room import Room
from classData.player import Player
from classData.monster import Monster


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
    roomsList = []
    monstersList = []
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

    # Game loop
    while continueGame != "exit":

        room = roomsList[currentRoomIndex]
        print("************************")
        print()
        room.describe_room()
        for monster in monstersList:
            if monster.startRoom == room.roomNumber:
                print("There is a monster in the room! Enough talk, have at you!")
                print()
                monster.describe_monster()
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
            commandNoun = commandList[1]

            if commandVerb == "get":
                newItem = room.get_item(commandNoun)
                if len(newItem) > 0:
                    player.add_item(newItem)
                    player.print_inventory()
                else:
                    print(commandNoun, "is not in the room.")

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
