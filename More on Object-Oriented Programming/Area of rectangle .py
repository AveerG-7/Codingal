class Rectangle:
    def __init__(self, l , w):
        self.l = l
        self.w = w
    
    def rectangle_area(self):
        return self.l * self.w
a = int(input("Enter length"))
b = int(input("Enter width"))
obj = Rectangle(a,b)
print("The area of the rectangle is:", obj.rectangle_area())


