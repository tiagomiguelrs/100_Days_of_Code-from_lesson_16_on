from operator import truediv
from turtle import Turtle, Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.down, key="Down")

while True:
    screen.update()
    snake.move()
    sleep(0.2)