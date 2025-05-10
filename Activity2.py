class Flashcard:
    def __init__(self , word , meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+ self.meaning
flash=[]
print("Welcome to flashcard application")
while(True):
    word=(input("Enter the word"))
    meaning=(input("Enter the meaning"))
    flash.append(Flashcard(word,meaning))
    option=int(input("Enter 0 to continue , enter 1 to stop"))
    if option:
        break
print("Your flashcards are:" )
for i in flash:
    print(i)