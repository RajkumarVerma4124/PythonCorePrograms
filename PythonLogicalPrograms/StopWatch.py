#Write a Stopwatch Program for measuring the time that elapses between the start and end clicks.

from datetime import datetime, date
class StopWatch:
    #Initializing start time by datetime
    def start(self):
        startTime = datetime.now().time()
        return startTime

    #defining stop time after start time using datetime
    def stop(self):
        stopTime = datetime.now().time()
        return stopTime

    #checking elapsed time between start time and stop time
    def timeElapsed(self, startTime, stopTime):
        elapsedTime = datetime.combine(date.today(),stopTime) - datetime.combine(date.today(),startTime)
        print(" Elapsed time :", elapsedTime)
        print(" Elapsed time :",elapsedTime.seconds,"seconds and ",elapsedTime.microseconds, "microseconds")

watchObj = StopWatch()
#defining the function for start,stop and elapsed time
print("Enter 1 to  START\nEnter 2 to STOP \nEnter 3 to Check Elapsed Time \nEnter 4 To EXIT")
while True:
    choice = int(input("Enter Your Choice : "))
    try:
        if ( choice == 1 ):
            startTime = watchObj.start()
        elif(choice == 2):
            stopTime = watchObj.stop()
        elif(choice == 3):
            elapseTime = watchObj.timeElapsed(startTime, stopTime)
        else:
            print("Enter The Right Option")
    except ValueError:
        print("Plese provide valid details ! ")


