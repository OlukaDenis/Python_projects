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
    begin_fill()
    speed(5)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "blue", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
