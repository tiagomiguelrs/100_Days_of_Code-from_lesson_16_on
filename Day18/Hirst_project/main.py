# import colorgram
#
# colors = colorgram.extract('Hirst_project_image.jpg', 30)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
#
# print(color_list)

from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.colormode(255)

final_color_list = [(179, 6, 93), (194, 76, 11), (208, 150, 9), (171, 18, 11), (175, 40, 135), (12, 201, 131),
                    (14, 142, 86), (40, 34, 162), (236, 225, 4), (236, 38, 32), (189, 58, 136), (40, 101, 153),
                    (5, 105, 59), (91, 68, 229), (111, 1, 42), (226, 229, 46), (17, 188, 202), (216, 146, 55),
                    (6, 71, 27), (110, 5, 2), (55, 192, 229), (6, 31, 106), (64, 208, 135), (3, 98, 107),
                    (50, 48, 216), (2, 246, 246), (76, 98, 7), (25, 239, 249), (176, 120, 149), (78, 239, 181)]

tim = Turtle()
tim.speed("fastest")
tim.ht()

def create_a_hirst(size):
    tim.penup()
    for row in range(10):
        tim.setx(-250)
        tim.sety(-250 + (row * 50))
        for col in range(10):
            tim.dot(size, choice(final_color_list))
            tim.fd(50)

create_a_hirst(15)

screen.exitonclick()