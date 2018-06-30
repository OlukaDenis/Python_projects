import turtle

denny = turtle.Turtle()
denny.getscreen().bgcolor()
denny.color("green", "green")
denny.speed(10)


def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/2)
            turtle.left(216)
        turtle.end_fill()
    
    
   
star(denny, 200)


turtle.done()
