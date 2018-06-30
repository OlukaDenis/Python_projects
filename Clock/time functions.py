from time import *
import time
from turtle import *

currentTime = strftime(" %H:%M:%S %p ", gmtime())
currentDate = strftime("%A %d %B %Y")
timeZone = strftime("Time-zone: %Z")
weekNumber = strftime("Week number: %W")

print(currentDate)
print(timeZone)
print(weekNumber)
print(currentTime)


color('aliceblue', 'blue')
begin_fill()
while True:
    speed(0)
    forward(200)
    left(170)
    forward(100)
    left(100)
    if abs(pos()) < 1:
        break
end_fill()
done()
    
