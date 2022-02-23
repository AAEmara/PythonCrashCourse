# Importing a specific function (make_pizza) 
# in pizza.py module that we made in the same file directory
# by using an alias for the function (as mp).
from pizza import make_pizza as mp

# Calling the function from the pizza module.
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')