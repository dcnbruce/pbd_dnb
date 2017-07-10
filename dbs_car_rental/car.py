# CA03
# Student ID: 10365675
# DBS Car Rental - Object Oriented Programming

class Car(object):
# Implement the car object.

    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
# Car colour
    def getColour(self):
        return self.__colour
# Car make
    def getMake(self):    
        return self.__make
# Car model
    def getModel(self):

        return self.__model
# Car miles
    def getMileage(self):
        return self.__mileage

    def setMake(self, make):
		self.__make = make

    def setColour(self, colour):
        self.__colour = colour

    def setModel(self, model):
        self.__model = model
		
    def setMileage(self, mileage):
        self.__mileage = mileage	

    def paint(self, colour):
        self.__colour = colour
		
    def move(self, distance):
        self.__mileage = self.__mileage + distance
# Car mileage on the clock
    def clock_mileage(self, distance):
        self.__mileage = self.__mileage + distance


class ElectricCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberDieselCylinders = 1

    def getNumberDieselCylinders(self):
        return self.__numberDieselCylinders

    def setNumberDieselCylinders(self, value):
        self.__numberDieselCylinders = value

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberVoltCells = 1

    def getNumberVoltCells(self):
        return self.__numberVoltCells

    def setNumberVoltCells(self, value):
        self.__numberVoltCells = value

class CarFleet(object):

    def __init__(self):
        self.__cars = []
        self.__numAvailable = 40
        
# number of cars available
    def getNumAvailable(self):
        return self.__numAvailable
# number of cars rented out
    def rentCar(self, numCars):
        self.__numAvailable -= numCars
        print('Available ' + str(self.__numAvailable))
# number of cars returned
    def returnCar(self, numCars):
        self.__numAvailable += numCars
        print('Available ' + str(self.__numAvailable))

