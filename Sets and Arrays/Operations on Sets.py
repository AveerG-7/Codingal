#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

my_set = {4,7,8,9,10,11,17,21,22,27,34,37,43,47}
print(my_set)

mixed_set = {1.0, "Hello", (1, 2, 3)}
print(mixed_set)

another_set = {1, 2, 3, 4, 3, 2,4}
print(another_set)

a_set = set([1, 2, 3, 2])
print(a_set)

the_set = [0, 1, 3, 4, 5]
print(the_set)

the_set.pop()
print(the_set)









