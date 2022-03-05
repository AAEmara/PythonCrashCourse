# Importing classes from separate modules.
from car_module import Car
from electric_car_module import ElectricCar

# Creating first instance of Car class.
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

# Creating first instance of ElectricCar class.
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())