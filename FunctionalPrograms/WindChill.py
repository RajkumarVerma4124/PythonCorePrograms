#A program that takes two double command-line arguments t and v and prints the wind chill.
import math
class WindChill:
    def findWindChill(self,t,v):
        if (t > 50 and v > 120 and v < 3):
            print("Enter the value within range thats is t < 50 and v < 120 and v > 3");
        else:
            temp = math.pow(v, 0.16)
            wind = round(35.74 + 0.6215 * t + 0.4275 * t - 35.75 * temp,3)
            print("The Wind Chill is ",wind, " ")


t = float(input("Enter the Temprature (in Fahrenheit) : "))
v = float(input("Enter the wind speed (in miles per hours) : "))
valueObj = WindChill()
valueObj.findWindChill(t,v)
