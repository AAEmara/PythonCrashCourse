# Importing Car class from car.py module file.
from car import Car

# Creating an object instance from the Car class.
my_new_car = Car('audi', 'a4', 2019)

# Printing the return of the method.
print(my_new_car.get_descriptive_name())
# Assigning a value for the odometer_reading attribute.
my_new_car.odometer_reading = 23
# Using the read_odometer method to print the odometer_reading attribute.
my_new_car.read_odometer()