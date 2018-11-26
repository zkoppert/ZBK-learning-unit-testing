#Define a Calculator Class
class calculator():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(a,b):
		return a+b
	def subtract(a,b):
		return a-b

#User Input
userInput=0

if userInput != 0:
	a=int(raw_input("Enter first number"))
	b=int(raw_input("Enter second number"))

#Create a Calculator that's ready to use
	a_calculator=calculator(a,b)

#Get Operation and display
	choice=1
	while choice != 0:
		print("0. Exit")
		print("1. Add")
		print("2. Subtract")
		choice=int(raw_input("Enter Choice: "))
		if choice == 1:
			print("Result: ", a_calculator.add())
		elif choice == 2:
			print("Result: ", a_calculator.subtract())
		elif choice == 0:
			print("Exiting")
		else:
			print("Invalid choice")

	print()
