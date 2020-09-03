#Program For Distance that takes two integer command-line arguments x and y and prints the Euclidean distance
import math
class Distance:
    def findEuclidean(self,x1Origin,y1Origin,x2Value,y2Value):
        distValue = math.sqrt(math.pow(x2Value - x1Origin, 2) + math.pow(y2Value - y1Origin, 2) * 1.0)
        distanceApprox = round(distValue,2)
        print("The Euclidean distance is : ",distanceApprox)

try:
    x1Origin = float(input("Enter the value of origin of x : "))
    y1Origin = float(input("Enter the value of origin y : "))
    x2Value = float(input("Enter the value of x : "))
    y2Value = float(input("Enter the value of y : "))
except ValueError:
    print("Please provide valid input!")
else:
    distData = Distance()
    distData.findEuclidean(x1Origin,y1Origin,x2Value,y2Value)