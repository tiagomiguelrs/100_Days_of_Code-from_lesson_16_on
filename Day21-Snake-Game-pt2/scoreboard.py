from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.ht()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 280)
        self.board_update()

    def board_update(self):
        self.write(arg=f"Score: {self.counter}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.counter += 1
        self.clear()
        self.board_update()

