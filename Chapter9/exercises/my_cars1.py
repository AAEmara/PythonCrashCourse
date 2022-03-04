# Importing multiple classes (Car, ElectricCar) from car.py module.
from car import Car, ElectricCar

# Creating an instance of gas vehicle from Car class.
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

# Creating an instance of electric vehicle from ElectricCar class.
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())