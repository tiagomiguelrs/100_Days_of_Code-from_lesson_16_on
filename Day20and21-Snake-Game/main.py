from turtle import Turtle, Screen

screen = Screen()
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

turtles = []

def start():
    for pos in range(3):
        turtle = Turtle(shape="square")
        turtles.append(turtle)












screen.exitonclick()