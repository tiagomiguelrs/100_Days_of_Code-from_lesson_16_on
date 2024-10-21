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


#-----------------------------------------------------------------------------------------------------------------------
# turtle_list = []
# init_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# def start():
#     for pos in init_positions:
#         turtle = Turtle(shape="square")
#         turtle.color("white")
#         turtle.penup()
#         turtle.goto(pos)
#         turtle_list.append(turtle)
#
#
# def move_fd(turtles: list):
#     screen.tracer(0)
#     for turtle in turtles:
#         turtle.fd(20)
#
#     sleep(0.5)
#     screen.update()
#
#
# def move_left(turtles: list):
#     screen.tracer(0)
#     for turtle_i in range(len(turtles)-1, 0, -1):
#         xpos = turtles[turtle_i-1].xcor()
#         ypos = turtles[turtle_i-1].ycor()
#         turtles[turtle_i].goto(xpos, ypos)
#     turtles[0].left(90)
#     turtles[0].forward(20)
#     sleep(0.5)
#     screen.update()


# screen.tracer(0)
# start()
# screen.update()
# move_left(turtle_list)

# def face_right():
#     snake.segments[0].setheading(0)
#
#
# def face_up():
#     snake.segments[0].setheading(90)
#
#
# def face_left():
#     snake.segments[0].setheading(180)
#
#
# def face_down():
#     snake.segments[0].setheading(270)