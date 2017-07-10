# cntl h 
# define my car class
class Car (object):
	def __init__(self):
		self.__make = 'Ferrari'
		self.__colour = 'Red'
		self.__mileage = 10
		# public variable
		self.engineSize = '5.4l'  

		
	def getMake(self):
		return self.__make
		
	def getColour(self):
		return self.__colour
	
	def getMileage(self):
		return self.__mileage
		
	def setMake(self, make):
		self.__make = make
		
	def setColour(self, colour):
		self.__colour = colour
		
	def setMileage(self, mileage):
		self.__mileage = mileage
	
	def move(self, distance):
		print 'Car has moved ' + str(distance) + ' kms. '
		self.__mileage = self.__mileage + distance
	
	def paint(self, colour):
		print 'Paint a car to colour :  ' + colour
		self.__colour = colour
		
class ElectricCar(Car):
	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCells = 1
	
	def getNumberFuelCells(self):
		return self.__numberFuelCells
		
	def setNumberFuelCells(self, value):
		self.__numberFuelCells = value

