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

# coração

# wn = turtle.Screen()
# wn.setup(width=600, height=600)
# red = turtle.Turtle()
# red.speed(0)
#
#
# def curve():
#     for i in range(200):
#         red.right(1)
#         red.forward(1)
#
#
# def heart():
#     red.fillcolor('red')
#     red.begin_fill()
#     red.left(140)


# Virus

# speed(10)
# color('cyan')
# bgcolor('black')
# b = 200
# while b > 0:
#     left(b)
#     forward(b * 3)
#     b = b - 1

# coração

# Creating a turtle object(pen)
pen = turtle.Turtle()


# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)


# Defining method to draw a full heart
def heart():
    # Set the fill color to red
    pen.fillcolor('red')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()


# Defining method to write text
def txt():
    # Move turtle to air
    pen.up()

    pen.speed(1)

    # Move turtle to a given position
    pen.setpos(-68, 95)

    # Move the turtle to the ground
    pen.down()

    # Set the text color to lightgreen
    pen.color('lightgreen')

    # Write the specified text in
    # specified font style and size
    pen.write("Te quiero Carolita!", move=True, font=(
        "Verdana", 12, "bold"))

# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()