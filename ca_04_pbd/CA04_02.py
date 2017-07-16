# Student ID 10365675 
# Date: 16 July 2017
# Programming for Big Data continuous assessment: No. 4b
# CA 04b: Lambda, map, filter reduce and list comprehension
#================================================
import math	
# Lambda is used in place of functions when it is not going to be repeated in the programme and is used with a name or anonymously.
#addition operation
add = reduce(lambda x, y: x+y, [7,8,9,10,11,12,14])
print "Using reduce with lambda on a list that is based on the addition operator is: ", add
# This returns the value of 71
print

#----------------------------------------------	
#subtraction operation
subtract = reduce(lambda x, y: x-y, [7,8,9,10,11,12,14])
print "Using reduce with lambda on a list that is based on the subtraction operator is: ", subtract
# This returns -57
print

#------------------------------------------------
#multiplication operation
multiply = reduce(lambda x, y: x*y, [7,8,9,10,11,12,14])
print "Using reduce with lambda on a list that is based on the multiplication operator is: ", multiply
#This returns 9313920
print

#------------------------------------------------
# Lambda and reduce use: Computing the factorial of a number and returning the result 
factorial = lambda x: reduce(lambda y, z: y*(z+1), range(x),1)
print factorial
print "The factorial of 6 is", factorial(6)
# Returns the value of 720
print
print "The factorial of 1 is", factorial(1)
print
# Returns the value of 1
print "The factorial of 0 is", factorial(0)
print
# Returns the value of 1
print "The factorial of 10 is", factorial(10)
# Returns the value of 3628800
print  

# trying out the factorial with multiplication and reduce function to find factorial 10. This must return a value of 3628800
def mult_fact(x,y):
	return x*y
u = [1,2,3,4,5,6,7,8,9,10]
w = reduce(mult_fact, u)
print "The reduced form of the list is: ", w
 # This returns a value of 3628800
print
#------------------------------------------------

#division operation
def divide(x, y):
	if x == 0:
		return 0
	if y == 0:
		return 'NaN'
	else:
		return x / y
x = [7,8,9,10,11,12,14]
y = [0,1,2,3,4,5,6]
answer = map(divide,x,y)
print "The mapping after the division operation is: ", answer
print

#------------------------------------------------
# Map use: Natural log notation taking a value of x on a list from 1 to 10 and returning log(x) of these numbers
def log(x) :
	if x <= 0:
# Number should be greater than zero	
		return 'INVALID'    
	return math.log(x)
y = [2,5,7,9,4,7, -1]
answer = map(log, y)
print "The mapping of natural log to a list of 7 numbers including a negative one returns the following list, the negative one returns 'invalid': ", answer

#The results of mapping natural log to a list of 7 numbers including a negative one returns the following list, the negative number returns 'invalid':  [0.6931471805599453, 1.6094379124341003, 1.9459101490553132, 2.1972245773362196, 1.3862943611198906, 1.9459101490553132, 'INVALID']
print
#------------------------------------------------

# Map and lambda use: List of squares
def square(values):
	return map(lambda x: x**2, values)
print "The result after mapping the square operator on the list is: ", square([47, 11, 42, 13])
# The result is [2209, 121, 1764, 169]
print
print "The result after mapping the square operator on the list is: ", square([20, 123, 36, 19])
# The result is [400, 15129, 1296, 361]
print
print "The result after mapping the square operator on the list is: ", square([-3, 12, 19, 14.3])
# The result is [9, 144, 361, 204.49]
print	
#------------------------------------------------

# Map and lambda use: List of square roots
def square_root(values):
	return map(lambda x: math.sqrt(x), values)	

print "The result after mapping the square root operator on the list is: ", square_root([2209, 121, 1764, 169])
# The result is  [47.0, 11.0, 42.0, 13.0]
print
print "The result after mapping the square root operator on the list is: ", square_root([47, 11, 42, 13])
print
# The result is [6.855654600401044, 3.3166247903554, 6.48074069840786, 3.605551275463989]
print
print "The result after mapping the square root operator on the list is: ", square_root([19, 36, 2309, 49, 625])
# The result is [4.358898943540674, 6.0, 48.05205510693585, 7.0, 25.0]
print
print "The result after mapping the square root operator on the list is: ", square_root([729, 1600, 36, 59, 10000])
# The result is [27.0, 40.0, 6.0, 7.681145747868608, 100.0]
print
	
#------------------------------------------------
# Map use: Using the Cube root to return a list of 6 values including negative roots	
print
def cuberoot(x):
	if x >= 0:
		return x**(1./3.)
	else:
		return -(-x)**(1./3.)

x = [-8, 27, 34, 8, -27, 126]
answer = map(cuberoot,x)
print "A list is returned with the roots of the cube root function as follows: ", answer
print
#A list is returned with the roots of the cube root function as follows: [-2.0, 3.0, 3.239611801277483, 2.0, -3.0, 5.0132979349645845]
print
	
#----------------------------------------------	
# Another lambda use for a cube operator	
cube = lambda x: x**3
print "The cube of 6 is: ",cube(6)
#returns the value 216
print
#------------------------------------------------
# Map use: Computing the power of a number and mapping the returned result 
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
		
x = [0,7,8,9,10,11,12,14]
y = [0,0,1,2,3,4,5,6]
answer = map(pow,x,y)

print "The result of x raised to the power y in the lists are as follows: ", answer
# Returns the values of	the following list:
# The results of x raised to the power y in the lists are as follows:  ['NAN', 1, 8, 81, 1000, 14641, 248832, 7529536]
print 

#------------------------------------------------
# Map use: Natural log notation taking a value of x on a list from 1 to 10 and returning log(x) of these numbers

list = [1,2,3,4,5,6,7,8,9,10]
natural_logarithm = map(lambda x:(math.log(x)), list)
print "The natural logarithm of all 10 numbers are: ",natural_logarithm  
# This prints the following list:  [0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196, 2.302585092994046] 
print 	

#----------------------------------------------	
#Map use: Multiplication notation taking a list of 14 numbers
def even_number(x):
	return x*2
	
list = [4,5,6,7,8,9,10,11,12,13,14,15,16,17]
even = map(even_number, list)
print "The result of mapping the list with their squares is: ", even
	# The application of map results in the following list:  [8,10,12,14,16,18,20,22,24,26,28,30,32,34]
print 

#------------------------------------------------
#Filter use: filtering a list of 20 values with a divisor of 3

divisor = [0,2,3,4,5,6,7,8,9,10,14,17,19,23,25,28,34,56,58,65]
remainder = filter(lambda x: x%3 == 0, divisor)
print "The result of using a divisor as a filter on a list is: ", remainder
# This filter function returns a list with 4 values (divisors of 3) as follows: [0, 3, 6, 9].
print

#------------------------------------------------

#Reduce use: reducing the values in a list using an addition function
mult = lambda x, y: x if (x > y) else y

additive = reduce(mult, [5, 55, 38, 25, 33, 16, 49, 42, 10, 60])
print "The reduction of the 10 values by reduce and lambda through an addition operation is: ", additive
# This returns a result of 60

print
#------------------------------------------------
#List comprehension use
# Using the cross product of three sets of lists to generate a list comprehension

set1 = [1,2,3,4,5,]
set2 = [2,4,6,8,10]
set3 = [6,7,8,9,10]
new_set = [(x,y,z) for x in set1 for y in set2 for z in set3]
print "The cross product of three sets to generate a new list as follows:", new_set

#The list generated is below:
#[(1, 2, 6), (1, 2, 7), (1, 2, 8), (1, 2, 9), (1, 2, 10), (1, 4, 6), (1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 4, 10), (1, 6, 6), (1, 6, 7), (1, 6, 8), (1, 6, 9), (1, 6, 10), (1, 8, 6), (1, 8, 7), (1, 8, 8), (1, 8, 9), (1, 8, 10), (1, 10, 6), (1, 10, 7), (1, 10, 8), (1, 10, 9), (1, 10, 10), (2, 2, 6), (2, 2, 7), (2, 2, 8), (2, 2, 9), (2, 2, 10), (2, 4, 6), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 4, 10), (2, 6, 6), (2, 6, 7), (2, 6, 8), (2, 6, 9), (2, 6, 10), (2, 8, 6), (2, 8, 7), (2, 8, 8), (2, 8, 9), (2, 8, 10), (2, 10, 6), (2, 10, 7), (2, 10, 8), (2, 10, 9), (2, 10, 10), (3, 2, 6), (3, 2, 7), (3, 2, 8), (3, 2, 9), (3, 2, 10), (3, 4, 6), (3, 4, 7), (3, 4, 8), (3, 4, 9), (3, 4, 10), (3, 6, 6), (3, 6, 7), (3, 6, 8), (3, 6, 9), (3, 6, 10), (3, 8, 6), (3, 8, 7), (3, 8, 8), (3, 8, 9), (3, 8, 10), (3, 10, 6), (3, 10, 7), (3, 10, 8), (3, 10, 9), (3, 10, 10), (4, 2, 6), (4, 2, 7), (4, 2, 8), (4, 2, 9), (4, 2, 10), (4, 4, 6), (4, 4, 7), (4, 4, 8), (4, 4, 9), (4, 4, 10), (4, 6, 6), (4, 6, 7), (4, 6, 8), (4, 6, 9), (4, 6, 10), (4, 8, 6), (4, 8, 7), (4, 8, 8), (4, 8, 9), (4, 8, 10), (4, 10, 6), (4, 10, 7), (4, 10, 8), (4, 10, 9), (4, 10, 10), (5, 2, 6), (5, 2, 7), (5, 2, 8), (5, 2, 9), (5, 2, 10), (5, 4, 6), (5, 4, 7), (5, 4, 8), (5, 4, 9), (5, 4, 10), (5, 6, 6), (5, 6, 7), (5, 6, 8), (5, 6, 9), (5, 6, 10), (5, 8, 6), (5, 8, 7), (5, 8, 8), (5, 8, 9), (5, 8, 10), (5, 10, 6), (5, 10, 7), (5, 10, 8), (5, 10, 9), (5, 10, 10)]
print
#------------------------------------------------
#Generator comprehension use
# Using an expression to list a set resulting a generator comprehension. The difference is to substitutes the square brackets in the list comprehension with round brackets. For very large databases, this will run a lot faster than using a list comprehension.

set1 = [1,2,3,4,5,]
set2 = [2,4,6,8,10]
set3 = [6,7,8,9,10]

new_set = ((x,y,z) for x in set1 for y in set2 for z in set3)
print "The cross product of three sets to get a  generator comprehension as follows:", new_set
# the next print line will print the results
for value in new_set: 	
	print value,

#The cross product of three sets to get a  generator comprehension as follows: <generator object <genexpr> at 0x0000000003079558>
#(1, 2, 6) (1, 2, 7) (1, 2, 8) (1, 2, 9) (1, 2, 10) (1, 4, 6) (1, 4, 7) (1, 4, 8) (1, 4, 9) (1, 4, 10) (1, 6, 6) (1, 6, 7) (1, 6, 8) (1, 6, 9) (1, 6, 10) (1, 8, 6) (1, 8, 7) (1, 8, 8) (1, 8, 9) (1, 8, 10) (1, 10, 6) (1, 10, 7) (1, 10, 8) (1, 10, 9) (1, 10, 10) (2, 2, 6) (2, 2, 7) (2, 2, 8) (2, 2, 9) (2, 2, 10) (2, 4, 6) (2, 4, 7) (2, 4, 8) (2, 4, 9) (2, 4, 10) (2, 6, 6) (2, 6, 7) (2, 6, 8) (2, 6, 9) (2, 6, 10) (2, 8, 6) (2, 8, 7) (2, 8, 8) (2, 8, 9) (2, 8, 10) (2, 10, 6) (2, 10, 7) (2, 10, 8) (2, 10, 9) (2, 10, 10) (3, 2, 6) (3, 2, 7) (3, 2, 8) (3, 2, 9) (3, 2, 10) (3, 4, 6) (3, 4, 7) (3, 4, 8) (3, 4, 9) (3, 4, 10) (3, 6, 6) (3, 6, 7) (3, 6, 8) (3, 6, 9) (3, 6, 10) (3, 8, 6) (3, 8, 7) (3, 8, 8) (3, 8, 9) (3, 8, 10) (3, 10, 6) (3, 10, 7) (3, 10, 8) (3, 10, 9) (3, 10, 10) (4, 2, 6) (4, 2, 7) (4, 2, 8) (4, 2, 9) (4, 2, 10) (4, 4, 6) (4, 4, 7) (4, 4, 8) (4, 4, 9) (4, 4, 10) (4, 6, 6) (4, 6, 7) (4, 6, 8) (4, 6, 9) (4, 6, 10) (4, 8, 6) (4, 8, 7) (4, 8, 8) (4, 8, 9) (4, 8, 10) (4, 10, 6) (4, 10, 7) (4, 10, 8) (4, 10, 9) (4, 10, 10) (5, 2, 6) (5, 2, 7) (5, 2, 8) (5, 2, 9) (5, 2, 10) (5, 4, 6) (5, 4, 7) (5, 4, 8) (5, 4, 9) (5, 4, 10) (5, 6, 6) (5, 6, 7) (5, 6, 8) (5, 6, 9) (5, 6, 10) (5, 8, 6) (5, 8, 7) (5, 8, 8) (5, 8, 9) (5, 8, 10) (5, 10, 6) (5, 10, 7) (5, 10, 8) (5, 10, 9) (5, 10, 10)
print
