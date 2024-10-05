#String Upper Case
#Outline:
#Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.

class IOstring:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string:")

    def print_string(self):
        print("The result of the string is: ",self.str1.upper())

str1 = IOstring()

str1.get_string()
str1.print_string()

