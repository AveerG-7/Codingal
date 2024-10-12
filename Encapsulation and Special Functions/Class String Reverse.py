#Class String Reverse
#Outline:
#Write a Python class to reverse a string word by word.

class class_reverse:
    def __init__(self,word):
        self.word= word
    def reverse_word(self):

        return self.word[::-1]
    
w = str(input("Enter a word to be reversed:     "))
rev_word = class_reverse(w)
result = rev_word.reverse_word()
print("The reversed string of the",(w),"is:   " ,(result))


