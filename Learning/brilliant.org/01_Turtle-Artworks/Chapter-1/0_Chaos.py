from turtle import *
from random import *


color_list = ["red", "blue", "green", "black",
              "blue", "yellow", "green", "red", "blue"]
color(choice(color_list))


for i in range(60):
    forward(randint(50, 100))
    left(randint(50, 100))
    forward(randint(50, 100))
    # back(randint(50,100))
    # print(i)


bye()
