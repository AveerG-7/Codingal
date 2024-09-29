#Class Parrot
#Outline:
#Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

# create class

class Parrot:

# class attribute

    species = "bird"

# instance attribute

    def __init__(self, name, age):

        self.name = name

        self.age = age

# instantiate the Parrot class

Goat = Parrot("Verstappen" , 99)
Slow = Parrot("Lewis" , 57)

# access the class attributes

print("Goat is a {}".format(Goat.species))

print("Slow is also a {}".format(Slow.species))

# access the instance attributes

print("{} is {} years old".format( Goat.name, Goat.age))

print("{} is {} years old".format( Slow.name, Slow.age))

