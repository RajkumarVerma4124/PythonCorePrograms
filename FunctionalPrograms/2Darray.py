#A Program for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.

class Array2D:
    def print2DArray(self,arrChoice,rows,cols):
        arr = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if (arrChoice == 1):
                    try:
                        arrData = int(input("Enter The Data Of an Array : "))
                    except ValueError:
                        print("Please provide valid input!")
                    else:
                        arr[i][j] = arrData
                elif (arrChoice == 2):
                    try:
                        arrData = float(input("Enter The Data Of an Array : "))
                    except ValueError:
                        print("Please provide valid input!")
                    else:
                        arr[i][j] = arrData
                elif (arrChoice == 3):
                    try:
                        arrData = bool(input("Enter The Data Of an Array For False Entry Enter Blank Input : " ))
                    except ValueError:
                        print("Please provide valid input!")
                    else:
                        arr[i][j] = arrData
                else:
                    print("No Values Selected")
        for row in arr:
            print(row)
try:
    arrChoice = int(input("Define The Values You Want To Enter 1.Int 2.Doubles 3.Booleans : "))
    arrSize = int(input("Enter The Size Of an Array : "))
except ValueError:
    print("Please provide valid input!")
else:
    rows, cols = (arrSize, arrSize)
    arrData = Array2D()
    arrData.print2DArray(arrChoice,rows,cols)
