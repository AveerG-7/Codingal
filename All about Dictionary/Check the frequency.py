test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1 }

print("Original dictionary :"+ str(test_dict))

K= int(input("Enter the number to check frequency in test_dict"))

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of the K is: " +str(res))
