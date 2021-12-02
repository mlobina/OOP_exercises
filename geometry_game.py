from random import randint


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


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


if __name__ == "__main__":
    while True:
        rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                              Point(randint(10, 19), randint(10, 19)))

        print(f"Rectangle Coordinates: ({rectangle.point1.x}, {rectangle.point1.y})"
              f" and ({rectangle.point2.x}, {rectangle.point2.y})")

        user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))

        print(f"Your point is inside rectangle: {user_point.falls_in_rectangle(rectangle)}")

        user_area = float(input("Guess rectangle area: "))

        print(f"Your area is: {rectangle.calculate_area() == user_area}")

        if (str(input("Do you want to try again? (yes/no) "))) == "yes":
            continue
        else:
            print("See you later")
            break







