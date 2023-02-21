# import colorgram
""" Colorgram.py is a python library that lets you extract colors from images."""
#
# rgb_colors = []
# colors = colorgram.extract('hirstimage.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
"""The above code is used to extract colors from hirstimage.jpg image  """

color_list = [ (231, 228, 224), (236, 220, 225), (225, 236, 229), (242, 161, 37), (18, 95, 180), (207, 75, 98), (51, 124, 59), (245, 219, 44), (156, 7, 57), (219, 116, 164), (241, 156, 175), (99, 201, 183), (11, 17, 79), (15, 60, 145), (73, 37, 8), (226, 166, 12), (251, 224, 0), (160, 172, 191), (16, 179, 13)]

import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)


def color_mode():
    color = random.choice(color_list)
    r = color[0]
    g = color[1]
    b = color[2]
    new_color = (r, g, b)
    return new_color

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, color_mode())
    tim.penup()
    tim.fd(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.penup()
        tim.forward(500)
        tim.setheading(0)




screen = Screen()
screen.exitonclick()
