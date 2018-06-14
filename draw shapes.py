import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    #Create a turtle denny to draw a circle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    for i in range(1,72):
        draw_square(brad)
        brad.right(5)

    #Create a turtle denny to draw a circle
    denny = turtle.Turtle()
    denny.shape("arrow")
    denny.color("blue")
    denny.circle(100)

    #a turtle to draw a triangle
    #oluk = turtle.Turtle()
    #oluk.shape("arrow")
    #oluk.color("red")
    #oluk.triangle(100)
    #oluk.right(90)


    window.exitonclick()

draw_art()
