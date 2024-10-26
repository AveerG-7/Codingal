# Python program to overload equality
# and less than operators

class A:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is less than ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
				
ob1 = A(int(input("Enter a number")))
ob2 = A(int(input("Enter a number")))
print("Passed Values :", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = A(int(input("Enter a number")))
ob4 = A(int(input("Enter a number(enter the same number enter previously)")))
print("Passed Values :", ob3.a, ob4.a)
print(ob3 == ob4)