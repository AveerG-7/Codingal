import random 

class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple':'red','orange':'orange','mango':'yellow','banana':'yellow','watermelon':'green'}


    def quiz(self):
        while(True):
            fruit,color = random.choice(list(self.fruit.items()))

            print("What is the colour of {}".format(fruit))
            ans = input()
            if (ans.lower() == color ):
                print("answer is correct")
            else:
                print("answer is wrong")

            option = int(input("Enter 0 if you want to play more else enter 1"))
            if (option):
                break

print("Welcome to the fruit quiz")
fq = FruitQuiz()
fq.quiz()



