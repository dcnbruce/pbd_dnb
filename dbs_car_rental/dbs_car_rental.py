# CA03
# Student ID: 10365675
# DBS Car Rental - Object Oriented Programming


from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, CarFleet

# Assumptions: There are only four types of cars: each class type has the same specifications, colour and mileage. For example there are 20 green Toyota Yaris cars of the petrol class. Similarly, there are four pearl-coloured Tesla Model S electric cars
print
print
print 'Welcome to DBS Car Rental'
print 
print 'Please make a selection from our car pool. We are the leading \n rental of hybrid and electric cars in Ireland'
print '--------------------------------------------------------------'
print
# The different specifications for the four categories of cars
# Electric car
car1 = ElectricCar()
car1.setMake('Tesla')
car1.setModel('Model S')
car1.setColour('Pearl')
car1.setMileage(523)
car1.setNumberFuelCells(2)
print 'Electric car type: ' + car1.getMake()
print 'Model: ' + car1.getModel()
print 'Colour: ' + car1.getColour()
print 'Number of fuel cells: ' + str(car1.getNumberFuelCells())
print 'Mileage on the clock: ' + str(car1.getMileage())
print '------------------'

#Petrol car
car2 = PetrolCar()
car2.setMake('Toyota')
car2.setModel('Yaris')
car2.setColour('Green')
car2.setMileage(653)
car2.setNumberCylinders(4)
print 'Petrol car type: ' + car2.getMake()
print 'Model: ' + car2.getModel()
print 'Colour: ' + car2.getColour()
print 'Number of cylinders: ' + str(car2.getNumberCylinders())
print 'Mileage on the clock: ' + str(car2.getMileage())
print '------------------'


# Diesel car
car3 = DieselCar()
car3.setMake('Ford')
car3.setModel('Mondeo')
car3.setColour('Black')
car3.setMileage(2500)
car3.setNumberDieselCylinders(6)
print 'Diesel car type: ' + car3.getMake()
print 'Model: ' + car3.getModel()
print 'Colour: ' + car3.getColour()
print 'Number of cylinders: ' + str(car3.getNumberDieselCylinders())
print 'Mileage on the clock: ' + str(car3.getMileage())
print '------------------'

# Hybrid car
car4 = HybridCar()
car4.setMake('Ford')
car4.setModel('Fusion Hybrid')
car4.setColour('Blue')
car4.setMileage(600)
car4.setNumberVoltCells(28)
print 'Hybrid car type: ' + car4.getMake()
print 'Model: ' + car4.getModel()
print 'Colour: ' + car4.getColour()
print 'Number of volt cells: ' + str(car4.getNumberVoltCells())
print 'Mileage on the clock: ' + str(car4.getMileage())
print '------------------'

# DBS Rental Company with a fleet of 40 cars: 8 diesel, 8 hybrid, 4 electric and 20 petrol.
class DBS_Car_Rental(object):
# initializing the class object
    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

# setting up a function to define the current stock of the car fleet
    def current_stock(self):
        for i in range(4):
            self.electric_cars.append(ElectricCar())
        for i in range(20):
            self.petrol_cars.append(PetrolCar())
        for i in range(8):
            self.diesel_cars.append(DieselCar())
        for i in range(8):
            self.hybrid_cars.append(HybridCar())
			
# setting up a function to define the entire stock of the car fleet   
    def stock_count(self):
        print 'petrol cars in stock: ' + str(len(self.petrol_cars))
        print 'electric cars in stock: ' + str(len(self.electric_cars))
        print 'diesel cars in stock: ' + str(len(self.diesel_cars))
        print 'hybrid cars in stock: ' + str(len(self.hybrid_cars))  
		
# A function that prompts the user about car availability and car category availability
    def rent(self, car_list, quantity):
        if len(car_list) == 0:
            print 'Sorry, nothing to rent, please try again later'
            return
        if len(car_list) < quantity :
            print 'Not enough cars'  
            return
        total = 0  
        while total < quantity:
            car_list.pop()
            total = total + 1
			
# A function for users to communicate with DBS Rental Cars     
    def process_rental(self):
        
        selection = raw_input('Would you like to rent a car? Please select y for yes and n for no y/n: ')
        if selection == 'y':
            selection = raw_input('What type would you like? \nPlease enter p\e\d\h as follows:\n p for petrol,  e for electric,  d for diesel and  h for hybrid: ')
            quantity = int(raw_input('How many cars would you like to rent?: '))
            if selection == 'p':
                self.rent(self.petrol_cars, quantity) 
                
            elif selection == 'd':
                self.rent(self.diesel_cars, quantity)
                 
            elif selection == 'h':
                self.rent(self.hybrid_cars, quantity)
            else:    
                self.rent(self.electric_cars, quantity)
             
        self.stock_count()
#Allow users to continue or exit the program
dbs_car_rental = DBS_Car_Rental()
dbs_car_rental.current_stock()
proceed = 'y'
while proceed == 'y':
    dbs_car_rental.process_rental()
    proceed = raw_input('Enter y to continue or n to quit: ')

# Testing rentals and returns, see results in test_car.py file
car_fleet = CarFleet()
car_fleet.rentCar(5)
car_fleet.returnCar(2)
car_fleet.returnCar(3)
car_fleet.rentCar(7)
car_fleet.returnCar(3)
car_fleet.rentCar(36)