
# Student ID 10365675 
# Date: 16 June 2017
# Programming for Big Data continuous assessment: No. 1 
# CA 1: Test calculator program

import unittest

from calculator import log, tan, cos, sin, square, cube, cuberoot, sqrt, pow, divide, multiply, subtract, add, factorial
 
# test the calculator functionality
class TestCalculator(unittest.TestCase):

# Natural logarithm
	def testLog(self):
		self.assertEqual(0, log(1))
		self.assertEqual('INVALID', log(0))
		self.assertEqual(round(3.91202 , 5), round(log(50.) , 5))
		self.assertEqual(round(5.22036 , 5), round(log(185.) , 5))
		self.assertEqual(round(3.82428 , 5), round(log(45.8) , 5))	
		self.assertEqual(round(8.51719 , 5), round(log(5000.) , 5))
	

# Sine
	def testSin(self):
		self.assertEqual(round(0.5 , 4), round(sin(30.) , 4))
		self.assertEqual(0, sin(0))
		self.assertEqual(round(1. , 4), round(sin(90.) , 4))
		self.assertEqual(round(-0.0872 , 4), round(sin(185.) , 4))
		self.assertEqual(round(0.7071 , 4), round(sin(45.) , 4))	
		self.assertEqual(round(-0.9799 , 4), round(sin(-78.5) , 4))
	
# Cosine
	def testCos(self):
		self.assertEqual(round(0.5 , 1), round(cos(60.) , 1))
		self.assertEqual(round(1. , 1), round(cos(0.) , 1))
		self.assertEqual(round(0. , 1), round(cos(90.) , 1))
		self.assertEqual(round(-0.9962 , 4), round(cos(185.) , 4))
		self.assertEqual(round(0.7071 , 4), round(cos(45.) , 4))	
		self.assertEqual(round(0.9304 , 4), round(cos(-21.5) , 4))
	
# Tangent
	def testTan(self):
		self.assertEqual(round(1.732 , 3), round(tan(60.) , 3))
		self.assertEqual(round(0. , 1), round(tan(0.) , 1))
		self.assertEqual('NAN', tan(90))
		self.assertEqual(round(0. , 1), round(tan(180.) , 1))
		self.assertEqual(round(1 , 1), round(tan(45.) , 1))	
		self.assertEqual(round(-0.3939 , 4), round(tan(-21.5) , 4))
	
# Square
	def testSquare(self):
		self.assertEqual(round(4. , 2), round(square(2.) , 2))
		self.assertEqual(round(9. , 2), round(square(3.) , 2))
		self.assertEqual(0, square(0))
		self.assertEqual(round(0.25 , 2), round(square(0.5) , 2))	
		self.assertEqual(round(16. , 2), round(square(-4.) , 2))


# Cubic function
	def testCube(self):
		self.assertEqual(round(8. , 2), round(cube(2.) , 2))
		self.assertEqual(round(27. , 2), round(cube(3.) , 2))
		self.assertEqual(0, cube(0))
		self.assertEqual(round(0.125 , 3), round(cube(0.5) , 3))	
		self.assertEqual(round(-64. , 2), round(cube(-4.) , 2))
	
# Cube root
	def testCuberoot(self):
		self.assertEqual(round(2., 2), round(cuberoot(8.), 2))
		self.assertEqual(round(3., 2), round(cuberoot(27.), 2))
		self.assertEqual(0, cuberoot(0))
		self.assertEqual(round(0.793700525, 7), round(cuberoot(0.50), 7))	
		self.assertEqual(round((-4.), 2), round(cuberoot(-64.), 2))
	
# Square root
	def testSqrt(self):
		self.assertEqual(round(2., 2), round(sqrt(4.), 2))
		self.assertEqual(round(3., 2), round(sqrt(9.), 2))
		self.assertEqual(0, sqrt(0))
		self.assertEqual(round(0.70710678, 8), round(sqrt(0.5), 8))	

# X to the power of Y
	def testPow(self):
		self.assertEqual(4, pow(2, 2))
		self.assertEqual(-8, pow(-2, 3))
		self.assertEqual(1, pow(2, 0))
		self.assertEqual('NAN', pow(0, 0))
		self.assertEqual(6, pow(6, 1))
		self.assertEqual(round(-(1/8.0), 4), round(pow(-2.0, -3), 4))

# Division
	def testDivide(self):
		self.assertEqual(3, divide(60, 20))
		self.assertEqual(-25, divide(100, -4))
		self.assertEqual(2, divide(-8, -4))
		self.assertEqual('NAN', divide(-2, 0))
		self.assertEqual(round(6/4.0, 4), round(divide(2/4.0, 2/6.0), 4))
	
# Multiplication
	def testMultiply(self):
		self.assertEqual(12, multiply(6, 2))
		self.assertEqual(40, multiply(10, 4))
		self.assertEqual(32, multiply(-4, -8))
		self.assertEqual(4, multiply(-2, -2))
		self.assertEqual(round(1/6.0, 4), round(multiply(2/4.0, 2/6.0), 4))
	
# Subtraction
	def testSubtract(self):
		self.assertEqual(4, subtract(6, 2))
		self.assertEqual(6, subtract(10, 4))
		self.assertEqual(-6, subtract(-14, -8))
		self.assertEqual(0, subtract(-2, -2))
		self.assertEqual(round(1/6.0, 4), round(subtract(2/4.0, 2/6.0), 4))
	
# Addition
	def testAdd(self):
		self.assertEqual(4, add(2, 2))
		self.assertEqual(6, add(2, 4))
		self.assertEqual(-6, add(2, -8))
		self.assertEqual(0, add(-2, 2))
		self.assertEqual(round(5/6.0, 4), round(add(2/4.0, 2/6.0), 4))

# Factorial
	def testFactorial(self):
		self.assertEqual(120, factorial(5))
		self.assertEqual(1, factorial(1))
		self.assertEqual(1, factorial(0))
		self.assertEqual(720, factorial(6))
		self.assertEqual(3628800, factorial(10))
		self.assertEqual('inf', factorial(-3))

if __name__== '__main__':
	unittest.main()