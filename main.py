# import colorgram
# colors = colorgram.extract('DH.jpg', 42)
# print(colors)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle
from turtle import Screen
import random
colors = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
          (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227),
          (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210),
          (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83),
          (245, 205, 7), (35, 88, 88), (103, 24, 56)]

screen = Screen()
turtle.colormode(255)
turtle.penup()
turtle.speed("fastest")
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
for _ in range(10):
    for _ in range(10):
        turtle.hideturtle()
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.back(500)
screen.exitonclick()
