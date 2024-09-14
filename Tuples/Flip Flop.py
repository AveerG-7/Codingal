# function to check whether palindrome or not
def palind(r):
	e = len(r) -1
	s = 0
	while(s<e):
		if(r[s]!=r[e]):
			return False
		s+=1
		e-=1
	return True


r = input("Enter:")

if(palind(r)):
	print("The Tuple is a palindrome")
else:
	print("The Tuple is not a palindrome")