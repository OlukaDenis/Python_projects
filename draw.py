import turtle
import math
import random

def draw():
    window = turtle.Screen()
    window.bgcolor("black")

    denny = turtle.Turtle()
    denny.color("white")
    denny.speed(0)
    rotate=int(360)
    def draw_circle(t, size):
        for i in range(10):
            t.circle(size)
            size-=4
    def drawUnique(t, size,repeat):
        for i in range(repeat):
            draw_circle(t, size)
            t.right(360/repeat)
    drawUnique(denny, 80, 10)

    denny = turtle.Turtle()
    denny.color("cyan")
    denny.speed(0)
    rotate=int(360)
    def draw_circle(t, size):
        for i in range(10):
            t.circle(size)
            size-=3
    def drawUnique(t, size,repeat):
        for i in range(repeat):
            draw_circle(t, size)
            t.right(360/repeat)
    drawUnique(denny, 60, 10)

    denny = turtle.Turtle()
    denny.color("yellow")
    denny.speed(0)
    rotate=int(360)
    def draw_circle(t, size):
        for i in range(10):
            t.circle(size)
            size-=2
    def drawUnique(t, size,repeat):
        for i in range(repeat):
            draw_circle(t, size)
            t.right(360/repeat)
    drawUnique(denny, 40, 10)

    


    

draw()
