#A Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 is the Computer and the Player 2 is the user.

import random,sys
class TicTacToe:
    # initialize list of "-" indicating empty position
    def reset(self):
        for dummy_positions in range(0, 9):
            board.append("-")

    # prints list in board format
    def printBoard(self):
        for position, value in enumerate(board):
            print(value, end=' ') if position not in (2, 5) else print(value)
        print()
        print()

    # checks for toss winner using random
    def checkToss(self):
        try:
            inputChoice = int(input("Enter toss(0,1) : "))
            if inputChoice not in (0, 1):
                raise Exception("Please enter valid choice between 1 and 0 ! ")
        except Exception:
            startGame.checkToss()
        else:
            randomNumber = random.randint(0,1)
            startGame.computeTurn(randomNumber, inputChoice)

    # computes who will play first and sets turn to that player
    def computeTurn(self,randomNumber, inputChoice):
        global player, computer, turnFlag, numberOfMoves
        if randomNumber == inputChoice:
            try:
                userChoice = input("Please enter X or O ! : ").upper()
                if userChoice != "X" and userChoice != "O":
                    raise Exception("Please enter valid choice ! ")
            except Exception:
                startGame.computeTurn(randomNumber, inputChoice)
            else:
                player = userChoice
                if player == "X":
                    computer = "O"
                    turnFlag = "player"
                else:
                    computer = "X"
        else:
            print("You lost the Toss ! ")
            computer = random.choice(["X", "O"])
            if computer == "X":
                turnFlag = "computer"
                player = "O"
            else:
                player = "X"

    # puts X or O for player at given place and computer at random place which is not occupied
    def play(self):
        global player, computer, turnFlag, numberOfMoves
        winner = startGame.checkWin()
        if winner != "":
            print("The Player With Letter ", winner ," won! ")
            return
        if numberOfMoves == 0:
            print("Game Ties ")
            return
        if turnFlag == "player":
            try:
                location = int(input("Enter position From 1 To 9: "))
                if location > 9 or location == 0:
                    raise Exception("Invalid location ! ")
            except Exception:
                startGame.play()
            else:
                if board[location - 1] == "-":
                    board[location - 1] = player
                    turnFlag = "computer"
                    numberOfMoves -= 1
                else:
                    print("Please choose another location ! ")
            startGame.printBoard()
            startGame.play()
        else:
            startGame.compPlayToWin(computer)
            startGame.compPlayToWin(player)
            location = random.randint(0, 8)
            if board[location] == "-":
                board[location] = computer
                turnFlag = "player"
                numberOfMoves -= 1
                startGame.printBoard()
            startGame.play()

    def playerTurnsChange(self):
        global turnFlag,numberOfMoves
        #startGame.checkWin()
        turnFlag = "player"
        if ( numberOfMoves == 0 ):
            print("Game Ties ")
            sys.exit(0)
        else:
            startGame.play()

    def playBoardPosition(self,position):
        global numberOfMoves
        print("MovesLeft",numberOfMoves)
        board[position]=computer
        numberOfMoves -= 1
        startGame.printBoard()
        startGame.playerTurnsChange()

    def winPlay(self,i1, i2, i3,checkCompWin):
        if( board[i1] == board[i2] and board[i1] != "-" and board[i3] == "-" and board[i1] == checkCompWin):
            startGame.playBoardPosition(i3)

        if (board[i1] == board[i3] and board[i1] != "-" and board[i2] == "-" and board[i1] == checkCompWin):
            startGame.playBoardPosition(i2)

        if(board[i3] == board[i2] and board[i3] != "-" and board[i1] == "-" and board[i2] == checkCompWin):
            startGame.playBoardPosition(i1)



    def compPlayToWin(self,checkPlayer):
        startGame.winPlay(0,1,2,checkPlayer)
        startGame.winPlay(3,4,5,checkPlayer)
        startGame.winPlay(6,7,8,checkPlayer)
        startGame.winPlay(0,4,8,checkPlayer)
        startGame.winPlay(2,4,6,checkPlayer)
        startGame.winPlay(0,3,6,checkPlayer)
        startGame.winPlay(1,4,7,checkPlayer)
        startGame.winPlay(2,5,8,checkPlayer)



    #  returns winner or null indicating no winner yet
    def checkWin(self):
        if startGame.checkRow() != "":
            return startGame.checkRow()
        if startGame.checkColumn() != "":
            return startGame.checkColumn()
        if startGame.checkDiagnol() != "":
            return startGame.checkDiagnol()
        if startGame.checkAlternateDiagnol() != "":
            return startGame.checkAlternateDiagnol()
        return ""


    # checks every row and returns winner or null.
    def checkRow(self):
        matchedRow = ""
        for rows in range(0, 8, 3):
            matchedRow = startGame.checkPairofThree(rows, rows + 1, rows + 2)
            if matchedRow != "":
                return matchedRow
        return matchedRow


    # checks every column and returns winner or null.
    def checkColumn(self):
        matchedColumn = ""
        for columns in range(0, 3):
            matchedColumn = startGame.checkPairofThree(columns, columns + 3, columns + 6)
            if matchedColumn != "":
                return matchedColumn
        return matchedColumn


    # checks diagonal and returns winner or null.
    def checkDiagnol(self):
        diagnols = 0
        return startGame.checkPairofThree(diagnols, diagnols + 4, diagnols + 8)


    # checks alternate diagonal and returns winner or null.
    def checkAlternateDiagnol(self):
        diagnols = 2
        return startGame.checkPairofThree(diagnols, diagnols + 2, diagnols + 4)


    # returns winner or null based on positions matched or not.
    def checkPairofThree(self,positionOne, positionTwo, positionThree):
        if board[positionOne] == board[positionTwo] == board[positionThree] and board[positionOne] != "-":
            return board[positionOne]
        return ""

startGame = TicTacToe()
board = []
turnFlag = ""
player = ""
computer = ""
winner = ""
numberOfMoves = 9
startGame.reset()
startGame.printBoard()
startGame.checkToss()
startGame.play()