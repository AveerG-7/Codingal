#Outline:
#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

class Computer:
    def __init__(self):
        self.max_price = 1000

    def sell(self):
        print("Selling price is: {}".format(self.max_price))

    def setmaxprice(self, price):
        self.max_price = price

a = Computer()
a.sell()

a.max_price = 100000
a.sell()

a.setmaxprice(10000)
a.sell()


