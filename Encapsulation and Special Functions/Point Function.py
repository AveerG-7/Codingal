#Point Function
#Outline:
#Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

class Point:
    def __init__(self, x = 0 , y = 0 ):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x , self.y)

p = Point(2,3)
print(p)
