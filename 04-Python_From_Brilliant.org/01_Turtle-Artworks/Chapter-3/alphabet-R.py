from turtle import *
speed(5)
width(15)

# draw the left stem
left(90)
forward(205)

# draw the loop
right(90)
forward(50)
for i in range(20):
    right(9)       # fix this line
    forward(8)
forward(40)

# draw the right leg
back(50)
left(120)
forward(120)

hideturtle()
bye()