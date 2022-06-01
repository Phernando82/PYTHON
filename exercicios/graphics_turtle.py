from turtle import *
import turtle

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
#
# col = ['yellow', 'red', 'pink', 'cyan', 'green', 'blue']
#
# for i in range(120):
#     t.pencolor(col[i])


# estrela

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# quadrado

# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
#
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
#
# turtle.done()


wn = turtle.Screen()
wn.setup(width=600, height=600)
red = turtle.Turtle()
red.speed(0)


def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)


def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
