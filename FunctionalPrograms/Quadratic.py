#A program to find the roots of the equation a*x*x + b*x + c
import cmath
class Quadratic:
    def findRoots(self,a,b,c):
        delta = b * b - (4 * a * c)
        print("Delta Value : ",delta)
        x1 = -b + cmath.sqrt(delta) / (2 * a)
        x2 = -b - cmath.sqrt(delta) / (2 * a)
        print("The Roots Of Quadratic Equation Are : ",x1, x2)


values = Quadratic()
try:
    a = int(input("Enter First value : "))
    b = int(input("Enter Second values : "))
    c = int(input("Enter Third values : "))
except ValueError:
        print("Please provide valid input!")
values.findRoots(a,b,c)