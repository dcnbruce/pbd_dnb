# car_app
from car import Car, ElectricCar	
my_car = Car()
# engine size is public and will be printed
print my_car.engineSize

# make it private and this will print an error
# print my_car.__make () # error here.

print my_car.getMake()
print my_car.getColour()
print my_car.getMileage()

my_car.engineSize = '10l'
print my_car.engineSize

my_car.setMake('BMW')
print my_car.getMake()

my_car.setColour('Silver')
print my_car.getColour()

my_car.setMileage(100)
print my_car.getMileage()

my_car.move(10)
print my_car.getMileage()

my_car.paint('blue')
print my_car.getColour()

electric_car = ElectricCar()
print electric_car.getNumberFuelCells()

electric_car.move(20)
print electric_car.getMileage()

