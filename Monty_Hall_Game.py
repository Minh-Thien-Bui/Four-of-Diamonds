import random

class Door:
    def __init__(self, number = 0, prize = False, chosen = False):
        self.__number = number
        self.__prize = prize
        self.__chosen = chosen

    def getNumber(self):
        return self.__number

    def getPrize(self):
        return self.__prize

    def getChosen(self):
        return self.__chosen

    def setNumber(self, number):
        self.__number = number
        
    def setPrize(self, prize):
        self.__prize = prize

    def setChosen(self, chosen):
        self.__chosen = chosen

def prizeDoor():
    grandPrize = random.randint(1, 3)
    
    for doorIndex in doors:
        if doorIndex.getNumber() == grandPrize:
            doorIndex.setPrize(True)

def chosenDoor():
    while True:
        try:
            initialChoice = eval(input("Please enter 1, 2, or 3 to choose a door: "))

            if initialChoice not in [1, 2, 3]:
                raise Exception()

            else:
                for doorIndex in doors:
                    if doorIndex.getNumber() == initialChoice:
                        doorIndex.setChosen(True)
                        print("\nYou have chosen Door Number " + str(initialChoice))
                        return doorIndex

        except:
            print("\nYou must enter a value between 1 and 3")

def eliminateDoor():
    for doorIndex in doors:
        if doorIndex.getPrize() == False and doorIndex.getChosen() == False:
            remainingDoors.append(doorIndex)

    randomDoor = random.choice(remainingDoors)
    remainingDoors.remove(randomDoor)
    
    print("\nMonty Hall has revealed that Door Number " + str(randomDoor.getNumber()) + " does not contain the prize\n")

def switchDoor():
    if not remainingDoors:
        for doorIndex in doors:
            if doorIndex.getPrize() == True:
                remainingDoors.append(doorIndex)
            
    for doorIndex in doors:
        if doorIndex.getChosen() == True:
            firstChoice = doorIndex
        if doorIndex.getPrize() == True:
            rightChoice = doorIndex
            
    switchChoice = remainingDoors[0]
    
    print("You may choose to stay with your initial choice of Door Number " + str(firstChoice.getNumber()) + " or switch to Door Number " + str(switchChoice.getNumber()))
    
    while True:
        try:
            stayOrSwitch = eval(input("Please enter 0 to stay or 1 to switch: "))

            if stayOrSwitch == 0:
                print("\nYou have chosen to stay with Door Number " + str(firstChoice.getNumber()))
                determineWinner(firstChoice, rightChoice)
                return

            elif stayOrSwitch == 1:
                print("\nYou have chosen to switch to Door Number " + str(switchChoice.getNumber()))
                determineWinner(switchChoice, rightChoice)
                return
                
            else:
                raise Exception()

        except:
            print("\nYou must enter either 0 or 1")

def determineWinner(finalChoice, rightChoice):
    print("\nThe prize is behind Door Number " + str(rightChoice.getNumber()))
                
    if finalChoice == rightChoice:
        print("\nYou picked the right door and won the Grand Prize!")
        
    else:
        print("\nYou picked the wrong door, but better luck next time")

def playAgain():
    while True:
        try:
            resetGame = eval(input("Please enter 0 to exit program or any other key to play again: "))

            if resetGame == 0:
                print("\nGame Over")
                return

            elif resetGame == 1:
                break
                
            else:
                raise Exception()

        except:
            print("\nYou must enter either 0 or 1")

    resetDoors()
    playGame()
    
def resetDoors():
    remainingDoors.clear()
    
    for doorIndex in doors:
        doorIndex.setPrize(False)
        doorIndex.setChosen(False)
    
def playGame():
    print("Welcome to the Monty Hall Gameshow\n\nThere are three doors and only one of them contains the grand prize.")
    
    prizeDoor()
    chosenDoor()
    eliminateDoor()
    switchDoor()
    playAgain()

doors = []
remainingDoors = []

for i in range(3):
    doors.append(Door(i + 1))
    
playGame()
