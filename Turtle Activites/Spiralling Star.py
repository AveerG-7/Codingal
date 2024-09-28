# Python program for drawing a Spiraling Polygon in Turtle   
# Importing the turtle Python library   
import turtle   
trtl = turtle.Turtle()  
  
# Taking the speed of turtle as 150  
trtl.speed(150)  
  
# Taking the legth of the side as 4 initially  
length = 4  
  
# Iterating the drawing 60 times overall  
for j in range(60):  
  
    # Making the turtle move forward by legth (units)  
    trtl.forward(length)  
    # Taking the exterior angle for a star shape as -144 degree,  
    # where -ve sign is used to draw the star upside down  
    trtl.right(-144)  
    # Updating the new length as 4 units shorter  
    # then the previous length  
    length = length - 4  
      
# Hiding the turtle after the completion of our drawing  
trtl.hideturtle()  