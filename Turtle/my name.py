#!/usr/bin/env python3
""" 
Developed on June, 15 2018 by Oluka Denis
The small circles are drawn by the circle
command.

"""

from turtle import *


def yin(radius, color1, color2):
    
    width(1)
    color("blue", color1)
    speed(10)
   
    begin_fill()
    circle(radius/2., 180)
    fd(20)
    left(90)
    fd(200)
    #circle(-radius/2., 180)
    end_fill()
    
def letterE():
    begin_fill()
    left(180)
    up()
    forward(radius/4)
    right(180)
    down()
    color(color1, color2)
    yin(200, "blue", "black")
    end_fill()
    
   """begin_fill()
    up()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)"""

def main():
    reset()
    yin(200, "blue", "white")
    #yin(200, "blue", "black")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
