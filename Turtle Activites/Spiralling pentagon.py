# Python program for drawing a Spiraling Polygon in Turtle   
# Importing the turtle Python library   
import turtle   
trtl = turtle.Turtle()  
  
# Taking the speed of turtle as 150  
trtl.speed(150)  
  
# Taking the length of the side as 2 initially  
length = 2  
  
# Iterating the drawing 55 times overall  
for j in range(55):  
  
    # Making the turtle move forward by length (units)  
    trtl.forward(length)  
    # Taking the exterior angle for a pentagon shape as 72 degrees  
    trtl.right(72)  
    # Updating the new length as 4 units shorter  
    # than the previous length  
    length = length - 4  
      
# Hiding the turtle after the completion of our drawing  
trtl.hideturtle()  