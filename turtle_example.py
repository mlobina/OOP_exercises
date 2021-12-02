import turtle
import tkinter as TK

# Create a canvas instance
my_turtle = turtle.Turtle()

# Don't draw a line
my_turtle.penup()
# Go to a certain coordinate
my_turtle.goto(50, 75)

# Draw a line
my_turtle.pendown()
my_turtle.forward(100)  # Move 100 pixels
my_turtle.left(90)  # Turn 90 degrees left
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(200)
turtle.done()

