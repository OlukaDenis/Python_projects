import time

#this program designed by oluka denis for a 12 hour time clock
seconds = 57
minutes = 59
hours = 2

while True:
    print(str(hours).zfill(2)+ ":" +str(minutes).zfill(2)+ ":" +str(seconds).zfill(2))
    seconds += 1
    time.sleep(1)
    if seconds  == 60:
        seconds = 0
        minutes += 1
        
    if minutes  == 60:
        minutes = 0
        hours += 1

    if hours  == 13:
        hours = 1
        

        
