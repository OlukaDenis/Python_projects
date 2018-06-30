import turtle
import math

denny = turtle.Turtle()
denny.getscreen().bgcolor()
denny.color("green", "green")
denny.speed(0)


def star(turtle, size):

    turtle.begin_fill()
    for i in range(5):
        turtle.forward(50)        
        turtle.left(216)
        
    turtle.penup()
    turtle.left(135)
    turtle.forward(100)
    turtle.pendown()
    turtle.end_fill()

    turtle.begin_fill()
    for j in range(8):
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(50)        
            turtle.left(216)
            
        turtle.penup()
        turtle.left(135)
        turtle.forward(100)
        turtle.pendown()
        turtle.end_fill()
    turtle.penup()
    turtle.backward(-100)
    turtle.pendown()
    turtle.end_fill()
    

   
star(denny, 30)


turtle.done()
