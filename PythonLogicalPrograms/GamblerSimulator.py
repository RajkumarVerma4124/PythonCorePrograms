#Simulates a gambler program who start with with some stakeMOney and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal.

import random,sys
class GamblerSimulator:
    #initializing the stake money and goal money
    def main(self):
        noOfBets = 0
        numberOfWins = 0
        try:
            stakeMoney = int(input("Enter Stake Amount You Have : "))
            goalMoney = int(input("Enter Goal Amount You Have : "))
        except ValueError:
            print("Plese provide valid details ! ")
            gameSimulator.main(self)
        else:
            gameSimulator.playGame(stakeMoney, goalMoney, noOfBets, numberOfWins)
    #playing game using random to define win and lose
    def playGame(self,stakeMoney, goalMoney, noOfBets, numberOfWins):
        sys.setrecursionlimit(99999999)
        randomNumber = random.randint(1,2)

        #checking stake money and goal money
        if gameSimulator.checkMoney(stakeMoney, goalMoney):
            gameSimulator.printResults(stakeMoney, goalMoney, noOfBets, numberOfWins)
            return
        #winning condition
        if randomNumber == 1:
            stakeMoney += 1
            numberOfWins += 1
        #losing condition
        else:
            stakeMoney -= 1
        noOfBets += 1
        gameSimulator.playGame(stakeMoney, goalMoney, noOfBets, numberOfWins)

    # checking stake money and goal money
    def checkMoney(self,stakeMoney, goalMoney):
        if (stakeMoney >= goalMoney or stakeMoney == 0):
            return True;

    #printing results after the game is finished
    def printResults(self,stakeMoney, goalMoney, noOfBets, numberOfWins):
        if stakeMoney != 0:
            print("You Have Won And Reached To The Goal Money Stage : ", goalMoney)
            print(f'Total number of Bets : {noOfBets}')
            print(f'Total number of Wins : {numberOfWins}')
            AverageWin = round((numberOfWins / noOfBets) * 100)
            print(f'Average win rate : {AverageWin}')
        else:
            print("You Have Loss All Your Money : ", goalMoney)


gameSimulator = GamblerSimulator()
gameSimulator.main()
