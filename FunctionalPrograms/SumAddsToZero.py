#A Program For Sum of three Integer adds to ZERO
class SumAddsToZero:
    def SumTheNumber(self,rangeOfArr,arrSize):
        count = 0
        for i in range(rangeOfArr):
            for j in range(rangeOfArr):
                for k in range(rangeOfArr):
                    if (arrSize[i] + arrSize[j] + arrSize[k] == 0):
                        count = count + 1
                        print("The Numbers That Adds To Zero are : ",arrSize[i]," " ,arrSize[j]," ",arrSize[k])

rangeOfArr = int(input("Enter The Range Of An Array : "))
arrSize = [ ]
for i in range(rangeOfArr):
    try:
        arrData = int(input("Enter the values : "))
    except ValueError:
        print("Dont Provide Empty Input ")
    arrSize.append(arrData)
print("The Data Are : ",arrSize)
arrNumbers = SumAddsToZero()
arrNumbers.SumTheNumber(rangeOfArr,arrSize)






