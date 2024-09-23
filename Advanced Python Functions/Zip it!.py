#Zip It!
#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary

str1 = (7,8,9)
str2 = ('a','b','c')
str3 = list(zip(str1,str2))
print(str3)

list1 = (7,8,9)
list2 = (9,8,7)

for x,y in zip(list1,list2[::-1]):
    print(x,y)

name1 = ("ronaldo","messi")
transfermarketfee = (100000000000000000000000000000000000000000000000000000000000000000000000000000000000000,0)

new_dict = {name1: transfermarketfee for name1,
                        transfermarketfee in zip(name1,transfermarketfee)}
print(new_dict)
