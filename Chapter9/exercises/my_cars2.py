# Importing the entire car.py module.
import car

# Creating instance of Car class.
my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

# Creating an instance of ElectricCar class.
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())