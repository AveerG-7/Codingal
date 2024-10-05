class Square:
    def __init__(self, s):
        self.s=s
    
    
    def square_area(self):
        return self.s * 4
a = int(input("Enter side dimensions"))
obj = Square(a)
print("The area of the square is:", obj.square_area())