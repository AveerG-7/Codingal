import math

# Base class

class Shape:

    def area(self):

        raise NotImplementedError("This method should be overridden in subclasses")

        # Derived class

class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return math.pi * (self.radius ** 2)

# Usage

if __name__ == "__main__":

# Create a Circle object

    radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)

# Calculate and print the area

print(f"The area of the circle with radius {radius} is: {circle.area()}")

