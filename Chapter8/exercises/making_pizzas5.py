# Importing all the functions in pizza.py module 
# that we made in the same file directory by using aestrisk (*).
# Not recommended for use since it could overwrite functions written in
# your program.
from pizza import *

# Calling the function from the pizza module.
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')