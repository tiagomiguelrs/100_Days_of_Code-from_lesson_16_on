from operator import truediv
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True

screen = Screen()
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.down, key="Down")

while game_on:
    screen.update()
    snake.move()
    sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()