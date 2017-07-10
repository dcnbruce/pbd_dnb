# Object Oriented Programming
# Student ID: 10365675
import unittest

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, CarFleet
from dbs_car_rental import DBS_Car_Rental


# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())
        self.car.setMileage(186)
        self.assertEqual(186, self.car.getMileage())
		
    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ford')
        self.assertEqual('Ford', self.car.getMake())
        self.car.setMake('Tesla')
        self.assertEqual('Tesla', self.car.getMake())
        self.car.setMake('Toyota')
        self.assertEqual('Toyota', self.car.getMake())
		
    def test_car_model(self):
        self.assertEqual('', self.car.getModel())
        self.car.setMake('Mondeo')
        self.assertEqual('Mondeo', self.car.getMake())
        self.car.setMake('Model S')
        self.assertEqual('Model S', self.car.getMake())
        self.car.setMake('Fusion Hybrid')
        self.assertEqual('Fusion Hybrid', self.car.getMake())	
        self.car.setMake('Yaris')
        self.assertEqual('Yaris', self.car.getMake())	

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('blue')
        self.assertEqual('blue', self.car.getColour())
        self.car.paint('pearl')
        self.assertEqual('pearl', self.car.getColour())
        self.car.paint('black')
        self.assertEqual('black', self.car.getColour())
        self.car.paint('green')
        self.assertEqual('green', self.car.getColour())
		
    def test_electric_car_fuel_cells(self):
        electric_car = ElectricCar()
        self.assertEqual(1, electric_car.getNumberFuelCells())
        electric_car.setNumberFuelCells(4)
        self.assertEqual(4, electric_car.getNumberFuelCells())
		
		
    def test_petrol_car_number_cylinders(self):
        petrol_car = PetrolCar()
        self.assertEqual(1, petrol_car.getNumberCylinders())
        petrol_car.setNumberCylinders(6)
        self.assertEqual(6, petrol_car.getNumberCylinders())
        petrol_car.setNumberCylinders(4)
        self.assertEqual(4, petrol_car.getNumberCylinders())
		
	def test_diesel_car_number_diesel_cylinders(self):
		diesel_car = DieselCar()
		self.assertEqual(1, diesel_car.getNumberDieselCylinders())
		diesel_car.setNumberDieselCylinders(4)
		self.assertEqual(4, diesel_car.getNumberDieselCylinders())

	def test_hybrid_car_number_volt_cells(self):
		hybrid_car = HybridCar()
		self.assertEqual(1, hybrid_car.getNumberVoltCells())
		hybrid_car.setNumberVoltCells(28)
		self.assertEqual(28, hybrid_car.getNumberVoltCells())		

    def test_car_fleet(self):
        car_fleet = CarFleet()
        self.assertEqual(40, car_fleet.getNumAvailable())


        car_fleet.rentCar(20)
        self.assertEqual(20, car_fleet.getNumAvailable())


        car_fleet.returnCar(5)
        self.assertEqual(25, car_fleet.getNumAvailable())


        car_fleet.returnCar(5)
        self.assertEqual(30, car_fleet.getNumAvailable())
		
        car_fleet.rentCar(7)
        self.assertEqual(23, car_fleet.getNumAvailable())
		
        car_fleet.returnCar(10)
        car_fleet.rentCar(33)

if __name__ == '__main__':
    unittest.main()		