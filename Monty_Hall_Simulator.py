# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:50:16 2021

@author: Minh Bui
"""

import random

class Player:
    def __init__(self, index = 0, choice = 0, stayOrSwitch = 0, stayCounter = 0, switchCounter = 0, winCounter = 0):
        self.__index = index
        self.__choice = choice
        self.__stayOrSwitch = stayOrSwitch
        self.__stayCounter = stayCounter
        self.__switchCounter = switchCounter
        self.__winCounter = winCounter
        
    def getIndex(self):
        return self.__index
    
    def getChoice(self):
        return self.__choice
    
    def getStayOrSwitch(self):
        return self.__stayOrSwitch
    
    def getStayCounter(self):
        return self.__stayCounter
    
    def getSwitchCounter(self):
        return self.__switchCounter
    
    def getWinCounter(self):
        return self.__winCounter
    
    def setIndex(self, index):
        self.__index = index
        
    def setChoice(self, choice):
        self.__choice = choice
        
    def setStayOrSwitch(self, stayOrSwitch):
        self.__stayOrSwitch = stayOrSwitch
        
    def setStayCounter(self, stayCounter):
        self.__stayCounter = stayCounter
        
    def setSwitchCounter(self, switchCounter):
        self.__switchCounter = switchCounter
        
    def setWinCounter(self, winCounter):
        self.__winCounter = winCounter
        
    def incrementStayCounter(self):
        self.__stayCounter += 1
        
    def incrementSwitchCounter(self):
        self.__switchCounter += 1
        
    def incrementWinCounter(self):
        self.__winCounter += 1

class Statistics:
    def __init__(self, gamesPlayed = 0, totalStays = 0, totalSwitches = 0, stayWins = 0, switchWins = 0):
        self.__gamesPlayed = gamesPlayed
        self.__totalStays = totalStays
        self.__totalSwitches = totalSwitches
        self.__stayWins = stayWins
        self.__switchWins = switchWins
        
    def getGamesPlayed(self):
        return self.__gamesPlayed
    
    def getTotalStays(self):
        return self.__totalStays
    
    def getTotalSwitches(self):
        return self.__totalSwitches
    
    def getStayWins(self):
        return self.__stayWins
    
    def getSwitchWins(self):
        return self.__switchWins
    
    def setGamesPlayed(self, gamesPlayed):
        self.__gamesPlayed = gamesPlayed
        
    def setTotalStays(self, totalStays):
        self.__totalStays = totalStays
        
    def setTotalSwitches(self, totalSwitches):
        self.__totalSwitches = totalSwitches
        
    def setStayWins(self, stayWins):
        self.__stayWins = stayWins
        
    def setSwitchWins(self, switchWins):
        self.__switchWins = switchWins

    def incrementGamesPlayed(self):
        self.__gamesPlayed += 1
        
    def incrementStayWins(self):
        self.__stayWins += 1
        
    def incrementSwitchWins(self):
        self.__switchWins += 1

class Door:
    def __init__(self, number = 0, prize = False):
        self.__number = number
        self.__prize = prize

    def getNumber(self):
        return self.__number

    def getPrize(self):
        return self.__prize

    def setNumber(self, number):
        self.__number = number
        
    def setPrize(self, prize):
        self.__prize = prize
        
def inputSimulations():
    while True:
        try:
            userInput = eval(input("How many simulations do you want to run?\nIf you enter a negative number, it will run a random number of simulations between zero and the absolute value of your input\nEnter the number of games you wish to simulate: "))

            if userInput >= 0:
                return round(userInput)

            else:
                randomSimulations = random.randint(0, abs(round(userInput)))
                return randomSimulations

        except:
            print("\nYou must enter a positive numerical value")

def prizeDoor():
    grandPrize = random.randint(1, 3)
    #print("\nPrize behind Door " + str(grandPrize))
    
    for doorIndex in doors:
        doorIndex.setPrize(False)
        
        if doorIndex.getNumber() == grandPrize:
            doorIndex.setPrize(True)

def calculateTotals(stats):
    stayTotal = 0
    switchTotal = 0
    
    for player in players:
        stayTotal += player.getStayCounter()
        switchTotal += player.getSwitchCounter()
        
    stats.setTotalStays(stayTotal)
    stats.setTotalSwitches(switchTotal)

def firstChoice(player):
    initialChoice = random.randint(1, 3)
    player.setChoice(initialChoice)
    #print("Player " + str(player.getIndex()) + " chose Door " + str(player.getChoice()))

def newChoice(player):
    if player.getIndex() == 3:
        if player.getStayOrSwitch() == 0:
            player.setStayOrSwitch(1)
        else:
            player.setStayOrSwitch(0)
        
    elif player.getIndex() == 4:
        randomDecision = random.randint(0, 1)
        player.setStayOrSwitch(randomDecision)

def eliminateDoor(player):
    for doorIndex in doors:
        if doorIndex.getPrize() == False and doorIndex.getNumber() != player.getChoice():
            remainingDoors.append(doorIndex)

    randomDoor = random.choice(remainingDoors)
    remainingDoors.remove(randomDoor)
    #print("Monty Hall eliminated Door " + str(randomDoor.getNumber()))
    
    if not remainingDoors:
        for doorIndex in doors:
            if doorIndex.getPrize() == True:
                remainingDoors.append(doorIndex)
    
    player.setChoice(remainingDoors[0].getNumber())
    remainingDoors.clear()

def finalChoice(player):
    if player.getStayOrSwitch() == 0:
        player.incrementStayCounter()
        #print("Player " + str(player.getIndex()) + " stayed with Door " + str(player.getChoice()))
    
    else:
        player.incrementSwitchCounter()
        eliminateDoor(player)   
        #print("Player " + str(player.getIndex()) + " switched to Door " + str(player.getChoice()))

def endGame(player):
    for door in doors:
        if door.getNumber() == player.getChoice():
            if door.getPrize() == True:
                player.incrementWinCounter()
                
                if player.getStayOrSwitch() == 0:
                    stats.incrementStayWins()
                    
                else:
                    stats.incrementSwitchWins()
                    
            return

def simulateGame(player):
    firstChoice(player)
    newChoice(player)
    finalChoice(player)
    endGame(player)

doors = []
remainingDoors = []
players = []
stats = Statistics()

for i in range(3):
    doors.append(Door(i + 1))
    
for i in range(4):
    players.append(Player(i + 1))
    
players[1].setStayOrSwitch(1)
gamesSimulated = inputSimulations()

for i in range(gamesSimulated):
    stats.incrementGamesPlayed()
    prizeDoor()
    
    for player in players:
        simulateGame(player)

calculateTotals(stats)

output = "\nGames Simulated: {totalGames}\nStay Total: {totalStays}\nSwitch Total: {totalSwitches}\n\nStay Wins: {stayWins}\nStay Losses: {stayLosses}\nStay Win Rate: {stayPercentage}%\n\nSwitch Wins: {switchWins}\nSwitch Losses: {switchLosses}\nSwitch Win Rate: {switchPercentage}%\n"

print(output.format(
    totalGames = stats.getGamesPlayed(), 
    totalStays = stats.getTotalStays(), 
    totalSwitches = stats.getTotalSwitches(), 
    
    stayWins = stats.getStayWins(), 
    stayLosses = stats.getTotalStays() - stats.getStayWins(),
    stayPercentage = round(100 * stats.getStayWins() / stats.getTotalStays(), 2),
    
    switchWins = stats.getSwitchWins(),
    switchLosses = stats.getTotalSwitches() - stats.getSwitchWins(),
    switchPercentage = round(100 * stats.getSwitchWins() / stats.getTotalSwitches(), 2)))

for player in players:
    playerResults = "Player {playerNumber} Win Total: {playerWins}\nPlayer {playerNumber} Loss Total: {playerLosses}\nPlayer {playerNumber} Win Rate: {playerPercentage}%\n"
    
    print(playerResults.format(
        playerNumber = player.getIndex(),
        playerWins = player.getWinCounter(),
        playerLosses = stats.getGamesPlayed() - player.getWinCounter(),
        playerPercentage = round(100 * player.getWinCounter() / stats.getGamesPlayed(), 2)))