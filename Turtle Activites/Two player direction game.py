# Python program to create a simple two player game using turtle  
# importing the random library  
import random  
# importing the turtle library  
import turtle  
  
# Method for checking whether the turtle  
# is in the Screen or its  not  
def isInScreen(win, tur):  
      
    # Finding the end bound of each corner of the turtle screen  
    leftBound = -win.window_width() / 2.7  
    rightBound = win.window_width() / 2.7  
    topBound = win.window_height() / 2.7  
    bottomBound = -win.window_height() / 2.7  
  
    # Finding the current position of turtle  
    ttlX = tur.xcor()  
    ttlY = tur.ycor()  
  
    # var for storing whether in the screen or not  
    stillIn = True  
  
    # condn for checking whether in screen or not  
    if ttlX > rightBound or ttlX < leftBound:  
        stillIn = False  
    if ttlY > topBound or ttlY < bottomBound:  
        stillIn = False  
  
    # the result being returned  
    return stillIn  
  
  
# Method for checking whether both the turtles have  
# a diff position or not  
def samepos(pink, green):  
    if pink.pos() == green.pos():  
        return False  
    else:  
        return True  
  
# main method  
def main():  
  
    # initializing the screen for turtle  
    wn = turtle.Screen()  
  
    # initializing the pink turtle by  
    # instantiating a new turtle object   
    # named 'pink'  
    pink = turtle.Turtle()  
      
    # setting the color of the pen to pink  
    pink.pencolor("pink")  
      
    # setting the size of the pen to 4.5  
    pink.pensize(4.5)  
      
    # setting the shape of the turtle to the classic turtle shape  
    pink.shape('turtle')  
    pos = pink.pos()  
  
    # initializing the green turtle by  
    # instantiating a new turtle object   
    # named 'green'  
    green = turtle.Turtle()  
      
    # setting the color of the pen to green  
    green.pencolor("green")  
      
  # setting the size of the pen to 4.5  
    green.pensize(4.5)  
      
    # setting the shape of the turtle to the classic turtle shape  
    green.shape('turtle')  
      
    # making the turtle hidden / invisible  
    green.hideturtle()  
      
    # lifting the (pen) turtle to not draw while moving  
    green.penup()  
      
    # moving the turtle (pen) to the new coordinates 50  
    # units away from the pink  
    green.goto(pos[0]+50, pos[1])  
      
    # making the turtle hidden / visible  
    green.showturtle()  
      
    # dropping the (pen) turtle to again start drawing when moving  
    green.pendown()  
  
    # variable for storing whether the turtles  
    # are in the screen or not  
    mT = True  
    jT = True  
  
    # Using while loop for playing the game  
    while mT and jT and samepos(pink, green):  
  
        # flipping of coin for pink  
        coinPink = random.randrange(0, 2)  
  
        # getting angle for Pink  
        # random.randrange(0, 180)  
        anglePink = 90  
  
        # condition to be used when left or right  
        # of the coin comes  
        if coinPink == 0:  
            pink.left(anglePink)  
        else:  
            pink.right(anglePink)  
  
      # flipping of coin for green  
        coinGreen = random.randrange(0, 2)  
  
        # getting angle for green  
        # random.randrange(0, 180)  
        angleGreen = 90  
  
        # condition to be used when left or right  
        # of the coin comes  
        if coinGreen == 0:  
            green.left(angleGreen)  
        else:  
            green.right(angleGreen)  
  
        # drawing for the Pink turtle  
        pink.forward(40)  
  
      # drawing for the Green turtle  
        green.forward(40)  
  
        # check whether the two turtles are in  
        # screen or not  
        mT = isInScreen(wn, green)  
        jT = isInScreen(wn, pink)  
  
    # setting the color of the pen for both pink and green turtles as black  
    pink.pencolor("black")  
    green.pencolor("black")  
  
    # condition for checking whether its a draw or a win  
    if jT == True and mT == False:  
        # printing the results  
        pink.write("Pink Won", True, align="center",  
                font=("arial", 15, "bold"))  
      
    elif mT == True and jT == False:  
          
        # printing the  results  
        green.write("Green Won", True, align="center",  
                font=("arial", 15, "bold"))  
    else:  
        # printing the results  
        pink.write("Draw", True, align="center",  
                font=("arial", 15, "bold"))  
        green.write("Draw", True, align="center",  
                font=("arial", 15, "bold"))  
  
    # exitting on closing  
    wn.exitonclick()  
  
  
# Calling the main method  
main()  