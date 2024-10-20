from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
screen = Screen()
screen.colormode(255)

# TODO-5 Create a function that generates random r, g and b colors
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# TODO-1 Draw a square
def draw_square(side):
    for _ in range(4):
        timmy.fd(side)
        timmy.right(90)


# TODO-2 Draw a dashed line
def dashed_line(times):
    for time in range(times):
        timmy.fd(10)
        timmy.penup()
        timmy.fd(10)
        timmy.pendown()


# TODO-3 Create a function that draws geometric forms from the triangle to the decangle
def draw_geometry():
    for _ in range(3, 11):
        angle = 360 / _
        timmy.pencolor(random_color())
        for side in range(_):
            timmy.fd(100)
            timmy.right(angle)


# TODO-4 Create a function that generates a random walk for the turtle
def random_walk(steps, speed):
    angles = [0, 90, 180, 270]
    timmy.width(5)
    timmy.speed(speed)
    for step in range(steps):
        timmy.pencolor(random_color())
        timmy.setheading(choice(angles))
        timmy.fd(10)


# TODO-6 Generate a random spirograph
def spirograph(n_circles, radius):
    angle = 360 / n_circles
    timmy.speed(0)
    for circle in range(n_circles):
        timmy.setheading(circle * angle)
        timmy.pencolor(random_color())
        timmy.circle(radius)


# draw_geometry()

# random_walk(500, 0)

spirograph(25, 100)


# timmy.penup()
# timmy.bk(300)
# timmy.pendown()
# dashed_line(25)




screen.exitonclick()