import random
class Fruit_Quiz:
    def __init__(self):
        self.fruit={"apple" : "red" , "Orange" : "orange" , "Banana" : "yellow"}
    def quiz(self):
        while(True):
            fruit,colour=random.choice(list(self.fruit.items()))
            print("What is the colour of " , fruit)
            user=input()
            if user.lower()==colour:
                print("Correct answer")
            else:
                print("Incorrect answer")
            option=int(input("Enter 0 to continue , enter 1 to stop"))
            if option:
                break
obj1=Fruit_Quiz()
obj1.quiz()
