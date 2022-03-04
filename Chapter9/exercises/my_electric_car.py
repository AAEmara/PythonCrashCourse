# Importing ElectricCar class from car.py module.
from car import ElectricCar

# Creating an object instance from the ElectricCar class.
my_tesla = ElectricCar('tesla', 'model s', 2019)

# Printing the return of the get_descriptive_name method.
print(my_tesla.get_descriptive_name())
# Using the output of other methods in the Battery class inherited 
# by ElectricCar class.
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()