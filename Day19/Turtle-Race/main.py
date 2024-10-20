from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color: ")

turtle_colors = ["red", "blue", "yellow", "orange", "green", "purple", "black", "gray", "dark blue", "dark green"]


def hatch_turtles(number_of_turtles: int):
    hatchlings = []
    for turtle in range(number_of_turtles):
        t = Turtle(shape="turtle")
        t.color(turtle_colors[turtle])
        t.speed("fastest")
        hatchlings.append(t)
    return hatchlings


def place_in_start(turtles: list):
    feet_appart = 30
    # Calculates how much of the y-axis all the turtles will occupy in a 500 height considering a space of feet_appart
    initial_y = -250 + ((500 - (feet_appart * len(turtles))) / 2)
    for turtle in range(len(turtles)):
        turtles[turtle].penup()
        turtles[turtle].goto(x=-240, y=initial_y + (turtle * feet_appart))


def race(turtles: list):
    for turtle in turtles:
        will_move = randint(0, 1)
        turtle.fd(will_move * 10)


# TODO-1 Create a function to use in the filter built-in function
def is_finished(turtle: Turtle):
    return turtle.xcor() >= 250

tim, tom, jan, jen, don, den = hatch_turtles(6)
my_turtles = [tim, tom, jan, jen, don, den]
place_in_start(my_turtles)

winner = []
racing = True
while racing:
    race(my_turtles)
    winner = [win for win in filter(is_finished, my_turtles)]
    # print(winner)
    if len(winner) > 0:
        racing = False

print(f"The winner is {winner[0].color()[0]}.")
if winner[0].color()[0] == user_bet:
    print("You won!")
else:
    print("You lost.")

screen.mainloop()