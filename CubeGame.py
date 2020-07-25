import json


# Function to validate move choices
# Returns true if a valid move choice
def validMove(moveChoice):
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

    if moveChoice in validMoves:
        print()
        return True
    elif moveChoice == "exit":
        exitGameMessage()
    else:
        print("You tried to move in your chosen direction and bumped into the wall. Try again.")
        print()

    return False


# Given a move choice, return the next room to move to
def getNextRoom(moveList, moveChoice):
    for moveDict in moveList:
        return moveDict[moveChoice]


# Print a kick butt intro, lol
def printIntro():
    print("Welcome to the mini dungeon, type exit to quit...")


def badMoveMessage():
    print("You can't go that way... Sorry!")
    print()


# Print exit game message
def exitGameMessage():
    print("Ok, bye - have a nice day...")
    print()
    print("Hope ya had fun, you filthy animal!")


# Main Function
def main():

    # defining some game variables
    currentRoom = "1"
    validMoves = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
    currentRoomIndex = int(currentRoom) - 1
    continueGame = ""

    # Open our game json
    with open('cube.json') as data_file:
        room_data = json.load(data_file)


    # Game loop
    while continueGame != "exit":
        print(room_data["rooms"][currentRoomIndex]["description"])
        moveChoice = input("Enter a cardinal direction to move (n,ne,e,se,s,sw,w,nw -->").lower()

        if validMove(moveChoice):
            moveList = room_data["rooms"][currentRoomIndex]["moves"]
            nextRoom = getNextRoom(moveList, moveChoice)

            if nextRoom != "0":
                currentRoomIndex = int(nextRoom)-1
            else:
                badMoveMessage()

        elif moveChoice.lower() == "exit":
            break

if __name__ == "__main__":
    main()
