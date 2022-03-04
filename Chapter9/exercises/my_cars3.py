# Importing every class from the car.py module.
# (not recommended!)
from car import *

# Creating instance of Car class.
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

# Creating an instance of ElectricCar class.
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())