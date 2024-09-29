#Class Vehicle
#Outline:
#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage 

audi = Vehicle(477,7000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004)
print("max_speed of audi=", audi.max_speed)
print("mileage of audi =", audi.mileage)

