from turtle import Turtle, Screen

tim = Turtle()


# TODO-1 Create function to go forward
def go_fd():
    tim.fd(10)


# TODO-2 Create a function to go backwards
def go_bk():
    tim.bk(10)


# TODO-3 Create a function to rotate left
def turn_left():
    tim.left(10)


# TODO-4 Create a function to rotate right
def turn_right():
    tim.right(10)


# TODO-6 Create a function that clears the screen
def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

# TODO-5 Call functions
Screen().onkeypress(fun=go_fd, key="w")
Screen().onkeypress(fun=go_bk, key="s")
Screen().onkeypress(fun=turn_left, key="a")
Screen().onkeypress(fun=turn_right, key="d")
Screen().onkeypress(fun=clear_screen, key="c")

Screen().listen()

Screen().exitonclick()