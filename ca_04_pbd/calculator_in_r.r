#CA04 Part 1: Programming for Big Data
# Student ID: 10365675
# Calculator function in R modified from CA01 - Python calculator program

#===============================================================================================

#1 function of a factorial
factorial_function <- function(x) {
  return(paste("The factorial of",x,"is",(factorial(x))))
}

# using test cases for factorial
factorial_function(5) # returns the value of 120
factorial_function(1)  # returns the value of 1
factorial_function(0)  # returns the value of 1
factorial_function(6)  # returns the value of 720
factorial_function(10)  # returns the value of 3628800

#---------------------------------------------------------------------------------------
#2 function for addition
add_function <- function(x,y) { 
  return(paste("The sum of",x,"and",y,"is",round(x+y, digits = 4)))
  }

# using test cases for addition
add_function (2,2)   # returns the value of 4
add_function (2,4)   # returns the value of 6
add_function (2,-8)  # returns the value of -6
add_function (-2,2)   # returns the value of 0
add_function (2/4,2/6)  # returns the value of 0.8333

#--------------------------------------------------------------------------------------
#3 function for subtraction
subtract_function <- function(x,y) { 
  return(paste("The subtraction of",y,"from",x,"is", round(x-y, digits = 4)))
}

# using test cases for subtraction
subtract_function (6,2)  # returns the value of 4
subtract_function (10,4)   # returns the value of 6
subtract_function (-14,-8)  # returns the value of 
subtract_function (-2,-2)   #returns the value of 0
subtract_function (2/4,2/6)  #returns the value of 0.17


#---------------------------------------------------------------------------------------
#4 function for multiplication
multiply_function <- function(x,y) { 
  return(paste("The multiplication of" ,x, "and" ,y, "is", round(x*y, digits = 4)))
}

# using test cases for multiplication
multiply_function (6,2)  # returns the value of 12
multiply_function (10,4)  # returns the value of 40
multiply_function (-4,-8)  # returns the value of 32
multiply_function (-2,-2)  # returns the value of 4
multiply_function (2/4,2/6)  # returns the value of 0.1667

#--------------------------------------------------------------------------------------------------------------
#5 function for division
divide_function <- function(x,y) { 
  return(paste(x, "divided by" ,y, "is", round(x/y, digits = 4)))
}

# using test cases for division
divide_function (60,20)  # returns the value of 3
divide_function (100,-4)  # returns the value of -25
divide_function (-8,-4)  # returns the value of
divide_function (-2,0)  # returns -Inf
divide_function (2/4,2/6)  # returns the value of 1.5

#-------------------------------------------------------------------------------------------------------------
#6 function for power function
power_function <- function(x,y) { 
  return(paste(x, "to the power of" ,y, "is", round(x**y, digits = 4)))
}

# using test cases for the power function
power_function (2,2)  # returns the value of 4
power_function (-2,3)  # returns the value of -8
power_function (2,0)  # returns the value of 1
power_function (0,0)  # returns the value of 1
power_function (6,1)  # returns the value of 6
# power_function (-2,-3) returns the value of -0.125 instead of -8. Please refer to rootfunction (#9) below for a corrected function.

#---------------------------------------------------------------------------------------------------------------
#7 function for square root function
sqrt_function <- function(x) { 
  return(paste("the square root of" ,x, "is", round(x^(1/2), digits = 4)))
}

# using test cases for the square root function
sqrt_function (4)  # returns the value of 2
sqrt_function (9)  # returns the value of 3
sqrt_function (0)  # returns the value of 0
sqrt_function (0.5)  # returns the value of 0.7071

#--------------------------------------------------------------------------------------------------------------------
#8 function for cube root function
cube_root_function <- function(x) { 
  return(paste("the cube root of" ,x, "is", round(x^(1/3), digits = 4)))
}

# using test cases for the cube root function
cube_root_function (8)  # returns the value of 2
cube_root_function (27)  # returns the value of 3
cube_root_function (0)  # returns the value of 0
cube_root_function (0.5)  # returns the value of 0.7937
#cube_root_function (-64) 
# the number R returns NaN for the cube root of -64 instead of -4  but this is the correct interpretation in R for real domain; the polyroot function in R will return the cubic root result. The way around this issue is to use the root function immediately below.

#------------------------------------------------------------------------------------------------------------------------
#9 return the (cube) root of both positive and negative numbers in R. This will work for most roots of real numbers.
rootfunction <- function(base, exponent) {
  x <- base/abs(base)
  y <- abs(base)^exponent
  root <- x * y
  return(paste("the (cube)root of the number is", round(root, digits = 4)))
  }

# using test cases for the cube root function or any other power or inverse roots
rootfunction (8, 1/3) # returns the value of 2
rootfunction (27, 1/3) # returns the value of 3
rootfunction (0, 1/3) # returns the value of NaN
rootfunction (0.5, 1/3) # returns the value of 0.7937
rootfunction (-64, 1/3)  # returns the value of 4

# further tests of the root function
rootfunction (64, 1/3) # returns the value of -4
rootfunction (-27, 1/3) # returns the value of -3
rootfunction (-8, 1/3)  # returns the value of -2

#---------------------------------------------------------------------------------------
#10 function for cube
cubic_function <- function(x) { 
  return(paste("the cube of" ,x, "is", round(x^3, digits = 4)))
}

# using test cases for the cubic function
cubic_function (2)  # returns the value of 8
cubic_function (3)  # returns the value of 27
cubic_function (0)    # returns the value of 0
cubic_function (0.5)    # returns the value of 0.125
cubic_function (-4)    # returns the value of -64

#----------------------------------------------------------------------------------------
#11 function for square 
squared_function <- function(x) { 
  return(paste("the square of" ,x, "is", round(x^2, digits = 4)))
}

# using test cases for the square root function
squared_function (2)   # returns the value of 4
squared_function (3)   # returns the value of 9
squared_function (0)    # returns the value of 0
squared_function (0.5)  # returns the value of 0.25
squared_function (-4)   # returns the value of 16

#-----------------------------------------------------------------------------------------
#12 function for cosine
cosine_function <- function(x)
{ 
  return(paste("the cosine of" ,x, "is", round(cos(x*0.0174532925), digits = 4)))
  }
         
# using test cases for the cosine function in degrees
cosine_function(60)   # returns the value of 0.5 
cosine_function(0)   # returns the value of 1 
cosine_function(90)    # returns the value of 0
cosine_function(185)   # returns the value of -0.9962  
cosine_function(-21.5)  # returns the value of 0.9304

#-------------------------------------------------------------------------------------------
#13 function for sine
sine_function <- function(x)
{ 
  return(paste("the sine of" ,x, "is", round(sin(x*0.0174532925), digits = 4)))
}

# using test cases for the sine function in degrees
sine_function(30)   # returns the value of 0.5 
sine_function(0)   # returns the value of 0 
sine_function(90)    # returns the value of 1
sine_function(185)   # returns the value of -0.0872  
sine_function(45)  # returns the value of 0.7071
sine_function(-78.5)  # returns the value of -0.9799

#---------------------------------------------------------------------------------------------
#14 function for tangent
tangent_function <- function(x)
{return(paste("The tangent of the degree is", round(tan(x*0.0174532925), digits = 4)))}

# using test cases for tangent function in degrees
tangent_function(60)   # returns the value of  1.7321 
tangent_function(0)   # returns the value of 0 
tangent_function(180)   # returns the value of 0  
tangent_function(45)  # returns the value of 1
tangent_function(-21.5)  # returns the value of -0.3939


#---------------------------------------------------------------------------------------------

#15 function of natural logarithm
logarithm_function <- function(x) {
  return(paste("The natural logarithm of",x,"is", round(log(x),digits = 4)))
  
} 

# using test cases for natural logarithm
logarithm_function(1) # returns the value of 0
logarithm_function(0)  # returns -Inf
logarithm_function(50) # returns the value of 3.912
logarithm_function(185)  # returns the value of 5.2204
logarithm_function(45.8)  # returns the value of 3.8243
logarithm_function(5000)  # returns the value of 8.5172

#---------------------------------------------------------------------------------------------
#14-1 tangent without using inbuilt R
new_function <- function(x) 
{
  if (x == -90 | x == 90 | x == 270 | x == -270 | x == 450)
  {return(paste("the tangent of" ,x, "is undefined"))} 
  else (x != -90 | x != 90 | x != 270 | x != -270 | x != 450) 
  {return(paste("The tangent of" ,x, "is", round(x*(360/pi)), digits = 4))
  }
}

# using test cases for tangent function in degrees; note, inbuilt R function for tan(x) returns values for tan 90, tan -90, etc instead of Nan or Undefined or Error.
tangent_function(60)   # returns the value of  1.7321 
tangent_function(0)   # returns the value of 0 
tangent_function(180)   # returns the value of 0  
tangent_function(45)  # returns the value of 1
tangent_function(-90)  # must return the value of -Inf or NaN but R isn't returning this.
tangent_function(90)  # must return the value of Inf or NaN but R isn't returning this.
tangent_function(270)  # must return the value of Inf or NaN but R isn't returning this.
tangent_function(-270)  # must return the value of -Inf or NaN but R isn't returning this.
tangent_function(-450)  # must return the value of -Inf or NaN but R isn't returning this.
#---------------------------------------------------------------------------------------------
# END