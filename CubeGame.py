import json
import random
import os
from classData.room import Room
from classData.player import Player
from classData.monster import Monster
from classData.item import Item
# from this article - https://stackoverflow.com/questions/22885780/python-clear-the-screen
from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command

roomsList = []
monstersList = []
itemsList = []

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear screen command as function of OS
    command = 'cls' if system_name().lower() == 'windows' else 'clear'

    # Action
    system_call([command])

# Game initialization
def game_init():

    print()
    printIntro()
    roomCount = len(roomsList)

    # First places items in any room
    for item in itemsList:
        itemPlaced = False
        while itemPlaced != True:
            randomRoom = random.randint(0, roomCount-1)
            currentRoom = roomsList[randomRoom]
            if currentRoom.event == "":
               currentRoom.place_item(item)
               roomsList[randomRoom] = currentRoom
               itemPlaced = True

    # Now places monsters in any room except the start
    for monster in monstersList:
        monsterPlaced = False
        while monsterPlaced != True:
            randomRoom = random.randint(1, roomCount-1)
            currentRoom = roomsList[randomRoom]
            if currentRoom.event == "":
                if currentRoom.monster is None:
                 currentRoom.place_monster(monster)
                 roomsList[randomRoom] = currentRoom
                 monsterPlaced = True

def debugRooms():
    for room in roomsList:
        print()
        print("*******************************************")
        print()
        room.describe_room()
        if room.monster != None:
            print("There is a monster here.")

def fightCheck(player):
    fight = False
    fightChoice = input("Will you purge this abomination? (y or n)").lower()

    while (fightChoice != "y") or (fightChoice != "n"):

        if fightChoice == "y":
            fight = True
            break
        elif fightChoice == "n":
            savingRoll = random.randint(1,10)
            if savingRoll <7:
                print("You couldn't flee!")
                fight = True
            else:
                newPlayerHP = (player.hp) - (player.hp * 0.1)
                player.hp = int(newPlayerHP)
                break
        else:
            print("I don't understand that choice, do y or n.")
            print()
    return fight


def combat(player, monster):
    victoryFlag = False
    print()
    print("What is a player? A miserable little pile of hit points! But enough talk, have at you!")
    while player.hp>0 and monster.HP>0:
        print()
        print("Test your might...")
        print()

        print("Your health is:", player.hp)
        print("The monster's health is:", monster.HP)
        print()

        input("Press enter to continue!")
        print()

        playerAttackPoints = 10
        playerAttackChance = random.randint(1,10)
        monsterAttackChance = random.randint(1,10)
        monsterAttackPoints = monster.attackDamage


        if player.weapon is None:
            print("You try to attack the monster unarmed!")
        else:
            playerAttackPoints = player.weapon.attackDamage
            print("You attack the monster with your", player.weapon.name, "!")
            print()
        if playerAttackChance > 4:
            print("The attack was a success!")
            print()
            if playerAttackChance == 10:
                print("CRITICAL HIT!")
                print()
                monster.HP = monster.HP - playerAttackPoints*2
                if monster.HP<0:
                    print("The monster's new health is 0")
                    print()
                else:
                    print("The monster's new health is:", monster.HP)
                    print()
            else:
                monster.HP = monster.HP - playerAttackPoints
                if monster.HP<0:
                    print("The monster's new health is 0")
                    print()
                else:
                    print("The monster's new health is:", monster.HP)
                    print()
        else:
            print("The attack missed!")
            print()

        input("Press enter to continue!")
        print()

        if monster.HP > 0:
            print("The monster uses", monster.attack, "!")
            print()
            if monsterAttackChance > 4:
                print("The monster's attack was a success!")
                print()
                if monsterAttackChance == 10:
                    print("CRITICAL HIT!")
                    print()
                    player.hp = player.hp - monsterAttackPoints * 2
                    if player.hp < 0:
                        print("Your new health is 0")
                        print()
                    else:
                        print("Your new health is:", player.hp)
                        print()
                else:
                    player.hp = player.hp - monsterAttackPoints
                    if player.hp < 0:
                        print("Your new health is 0")
                        print()
                    else:
                        print("Your new health is:", player.hp)
                        print()
            else:
                print("The attack missed!")
                print()
            input("Press enter to continue!")
            print()



    if player.hp>0:
        print("You have emerged from the combat victorious...")
        victoryFlag = True
    else:
        print("You have been slain... Game Over.")
        exit()
    return victoryFlag



# Print a kick butt intro, lol
def printIntro():
    print("Welcome to the mini dungeon, type exit to quit...")


# Print command options
def printHelp():
    print()
    print("You can enter a direction to move, like : n, ne, e, se, s, sw, w, nw, up or down")
    print("-- or --")
    print("You can enter a command such as 'get sword', 'inventory' or 'status'")
    print()



# Print exit game message
def exitGameMessage():
    print("All things must come to an end, and the game is no exception...")


# Main Function
def main():

    # define some game variables

    player = Player()
    currentRoom = "1"
    currentRoomIndex = int(currentRoom) - 1
    continueGame = ""
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw", "up", "down"]
    clearScreen = False

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

        if clearScreen:
            clear_screen()

        room = roomsList[currentRoomIndex]
        if room.event == "badWin" or room.event == "goodWin":
            print(room.eventDescription)
            break
        print("************************")
        print()
        room.describe_room()
        if room.monster == None:
            print("There are no monsters here. A brief respite may be had.")
            print()
        else:
            print("There is a monster in the room!")
            print()
            room.monster.describe_monster()
            print()
            if fightCheck(player)==True:
                if combat(player,room.monster)==True:
                    room.monster = None
            elif player.hp>0:
                print("You have evaded the monster for now, but in the process have suffered an injury. You now have", player.hp, "health.")
                print("If you do not flee immediately, you will encounter it again.")
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
                clear_screen()
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
        elif commandChoice.lower() == "debugrooms":
            debugRooms()
        elif commandChoice.lower() == "exit":
            break

        else:
            print("Sorry, I don't understand -->", commandChoice)

    exitGameMessage()



if __name__ == "__main__":
    main()
