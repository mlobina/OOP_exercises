from random import randint
import turtle
import tkinter as TK


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # Don't draw a line
        canvas.penup()
        # Go to a certain coordinate
        canvas.goto(self.point1.x, self.point1.y)
        # Draw a line
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)  # Move 100 pixels
        canvas.left(90)  # Turn 90 degrees left
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


if __name__ == "__main__":
    while True:
        rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                              Point(randint(10, 400), randint(10, 400)))

        print(f"Rectangle Coordinates: ({rectangle.point1.x}, {rectangle.point1.y})"
              f" and ({rectangle.point2.x}, {rectangle.point2.y})")

        user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))

        print(f"Your point is inside rectangle: {user_point.falls_in_rectangle(rectangle)}")

        if user_point.falls_in_rectangle(rectangle) is True:
            my_turtle = turtle.Turtle()
            rectangle.draw(canvas=my_turtle)
            user_point.draw(canvas=my_turtle)
            turtle.done()  # It's important to paste this after everything has completed drawing
        else:
            pass

        user_area = float(input("Guess rectangle area: "))

        print(f"Your area is: {rectangle.calculate_area() == user_area}")

        if (str(input("Do you want to try again? (yes/no) "))) == "yes":
            continue
        else:
            print("See you later")
            break







