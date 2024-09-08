# Function to create list of square of numbers
def SquaredValues(beg, end):
	lst = []
	# store all the values of square of numbers 
	# between given range in a list
	for i in range(beg, end):
		# append value to the list
		lst.append(i**2)

	lst_even = []
	lst_odd = []

	# check and store odd and even squares in seperate lists
	for i in lst:
		if i%2==0:
			# append value to the list
			lst_even.append(i)
		else:
			# append value to the list
			lst_odd.append(i)
	
	print("Here's a list of even squares within specified range", lst_even)
	print("Here's a list of odd squares within specified range", lst_odd)
	
# Take input from user for range of numbers	
beg = int(input("Enter starting range : "))
end = int(input("Enter end range : "))

# Function call
SquaredValues(beg, end)