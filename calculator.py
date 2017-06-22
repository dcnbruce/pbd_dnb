
# Student ID 10365675 
# Date: 16 June 2017
# Programming for Big Data continuous assessment: No. 1 
# CA 1: Calculator program with 10 + 4 functions



# Computing the factorial of a number and returning the result
def factorial(x):
	if x > 1:
		return x * factorial(x - 1)
	if x < 0:
		return 'inf'
	else:
# could also be 'return x' if 0! is not included		
		return 1     
				

# Computing the addition of two numbers and returning the result
def add(x, y):
		
	return x + y
		

# Computing the subtraction of a number ['y'] from another	number ['x'] and returning the result
def subtract(x, y):
	return x - y


# Computing the product of two numbers and returning the result	
def multiply(x, y):
	return x * y


# Computing the division two numbers and returning the result
def divide(x, y):
	if x == 0:
		return 0
	if y == 0:
		return 'NAN'
	else:
		return x / y


# Computing the power of a number and returning the result		
def pow(x, y):
	if x != 0 and y == 1 :
		return x
	if x ==0 and y ==0:
		return 'NAN'
	if x ==0 and y != 0 : 
		return 0
	if x !=0 and y ==0:
		return 1
	else:
		return x**y

			
# Computing the square root of a number	(x)	and returning the result
def sqrt(x):
	if x < 0 :
		return 'INVALID'
	if x>=0 :
		return x**(1./2.)

			
# Computing the cube root of a number (x) and returning the result
def cuberoot(x):
	if x >= 0:
		return x**(1./3.)
	else:
		return -(-x)**(1./3.)
			
# Computing the cube of a number (x) and returning the result		
def cube(x):
	if x >= 0:
		return x**(3.)
	else:
		return -(-x)**(3.)

# Computing the square of a number (x) and returning the result
			
def square(x):
	if x >= 0:
		return x**(2.)
	else:
		return (-x)**(2.)
			
# import math library

import math

# Computing the sine of a number (x) and returning the result in degrees

#def sin(x):
	#n = round((x/180) * 3.14159265358979 , 4)
	#return x - ((x**3)/factorial(3)) + ((x**5)/factorial(5)) - ((x**7)/factorial(7)) + ((x**9)/factorial(9)) - ((x**11)/factorial(11)) + ((x**13)/factorial(13)) - ((x**15)/factorial(15))
# This method gives an approximation which fails in the testing so we have to import math to create the function

def sin(x):
	return math.sin(math.radians (x))

# Computing the cosine of a number	(x)	and returning the result in degrees

#def cos(x) :
#x = round(((1-x)/180) * 3.14159265358979 , 2)
	#return 1 - ((x**2)/factorial(2)) + ((x**4)/factorial(4)) - ((x**6)/factorial(6)) + ((x**8)/factorial(8)) - ((x**10)/factorial(10)) + ((x**12)/factorial(12)) - ((x**14)/factorial(14)) + ((x**16)/factorial(16))
# This method gives an approximation which fails in the testing so we have to import math to create the function
		
def cos(x):
	return math.cos(math.radians (x))

# Computing the tangent of a number	(x)	and returning the result in degrees
# We use the import math from python library to create this function.

def tan(x):
		if x == 90 or x == 270 :
			return 'NAN'
		return math.tan(math.radians (x))

		
# Computing the natural logarithm of a number and returning the result
# We use the import math from python library to create this function.

def log(x) :
	if x <= 0:
# Number should be greater than zero	
		return 'INVALID'    
	return math.log(x)


import string

# Now we create user inputs and validate some of these so the calculator can be operational.

	
def calculator():
	print """This calculator allows one to calculate:
		 factorial, add, subtract, 
		multiply, divide, pow, sqrt, cuberoot, cube, square, sin, cos, tan, log
		"""
	# space	
	print "---------------------------------------------------------------"
	# space	
	print 

			
	print "Selection of  operation"
	print "---------------------------------------------------------------"	

# Operator selection

# Validating the selection is a number from 0 to 14		
	invalid = 1
	while invalid == 1 :
		invalid = 0
		
# Validating that user only selects a number
		
		selection = " "
		while selection is not int:
			try:
				selection = int(raw_input("""\n1 for Factorial \n2 to  Add  \n3 to Subtract \n4 to Multiply \n5 to Divide \n6 for Pow \n7 for Sqrt \n8 for Cuberoot \n9 for Cube \n10 for Square \n11 for Sin \n12 for Cos \n13 for Tan \n14 for Log \n\nPlease select any operator number above (must be 1 - 14):\n """))
				break
			except ValueError:
				print "Enter a valid number"
		
# Validating that the operator selected is between 1 and 14 (corresponding with the 14 functions created above)
		
		if selection < 0 or selection > 14:
			print "INVALID!, try a number from 1 to 14"

# User inputs to return operation
# And validating that only numbers are entered for the calculation of all 14 selections	

# Factorial
		while selection is not int:
			try:
				if selection == 1:
					x = int(input("Please enter a number: "))
					print 'The factorial result is: ' , factorial(x)
				break
			except ValueError:
				print "Enter a valid number"		

# Addition				
		while selection is not int:
			try:						
				if selection == 2:
					x = float(raw_input("Please enter first number: "))
					y = float(raw_input("Please enter second number: "))
					print 'The addition result is: ' , add(x, y)
				break
			except ValueError:
				print "Enter a valid number"	

# Subtraction				
		while selection is not int:
			try:		
				if selection == 3 :
					x = float(raw_input("Please enter first number: "))
					y = float(raw_input("Please enter second number: "))
					print 'the subtraction result is: ' , subtract(x, y)
				break
			except ValueError:
				print "Enter a valid number"

# Multiplication				
		while selection is not int:
			try:	
				if selection == 4 :
					x = float(raw_input("Please enter first number: "))
					y = float(raw_input("Please enter second number: "))
					print 'The multiplication result is: ' , multiply(x, y)
				break
			except ValueError:
				print "Enter a valid number"

# Division				
		while selection is not int:
			try:			
				if selection == 5 :
					x = float(raw_input("Please enter numerator: "))
					y = float(raw_input("Please enter denominator: "))
					print 'The division result is: ', divide(x, y)
				break
			except ValueError:
				print "Enter a valid number"					

# Exponentiation				
		while selection is not int:
			try:		
				if selection == 6:
					x = float(raw_input("Please enter number: "))
					y = float(raw_input("Please enter exponentiation: "))
					print 'The result of your exponentiation is: ', pow(x, y)
				break
			except ValueError:
				print "Enter a valid number"			

# Square root				
		while selection is not int:
			try:		
				if selection == 7:
					x = float(raw_input("Please enter a positive number: "))
					print 'The square root result of the number is: ', sqrt(x)
				break
			except ValueError:
				print "Enter a valid number"	

# Cube root				
		while selection is not int:
			try:		
				if selection == 8:
					x = float(raw_input("Please enter a number: "))
					print 'The cube root result of the number is: ', cuberoot(x)
				break
			except ValueError:
				print "Enter a valid number"	

# Cube				
		while selection is not int:
			try:		
				if selection == 9 :
					x = float(raw_input("Please enter a number: "))
					print 'The cubed result of the number is: ', cube(x)
				break
			except ValueError:
				print "Enter a valid number"

# Square				
		while selection is not int:
			try:		
				if selection == 10 :
					x = float(raw_input("Please enter a number: "))
					print 'The squared result of the number is: ', square(x)
				break
			except ValueError:
				print "Enter a valid number"		

# Sine (degrees)				
		while selection is not int:
			try:		
				if selection == 11 :
					x = float(raw_input("Please enter a number in degree format for its corresponding sine result: "))
					print 'The sin result of the number is: ', sin(x)
				break
			except ValueError:
				print "Enter a valid number"

# Cosine (degrees)				
		while selection is not int:
			try:		
				if selection == 12 :
					x = float(raw_input("Please enter a number in degree format for its corresponding cosine result: "))
					print 'The cosine result of the number is', cos(x)
				break
			except ValueError:
				print "Enter a valid number"	

# Tangent (degrees)				
		while selection is not int:
			try:		
				if selection == 13 :
					x = float(raw_input("Please enter a number in degree format for its corresponding tangent result: "))
					print 'The tangent result of the number is: ', tan(x)
				break
			except ValueError:
				print "Enter a valid number"		

# Natural logarithm (ln)				
		while selection is not int:
			try:		
				if selection == 14 :
					x = float(raw_input("Please enter a positive number for its natural logarithm result: "))
					print 'The natural logarithm result of the number is: ', log(x)
				break
			except ValueError:
				print "Enter a valid number"

		
# Making further operations or quitting the calculator program
		more_operations = raw_input("\n\nDo you want to make further calculations? Please enter Y to continue, or N to quit program: ")
				
#Validating that both lower and uppercase can be entered
		more_operations = string.upper(more_operations)
		
		if more_operations == "Y":
			more_operations = selection
			invalid = 1
			
calculator()








