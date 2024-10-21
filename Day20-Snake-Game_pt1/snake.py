from turtle import Turtle, Screen
from time import sleep

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(pos)
            self.segments.append(turtle)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            xpos = self.segments[segment - 1].xcor()
            ypos = self.segments[segment - 1].ycor()
            self.segments[segment].goto(xpos, ypos)
        self.head.fd(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)