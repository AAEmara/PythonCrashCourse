# Assigning cars into lists
cars = ['audi', 'bmw', 'subaru', 'toyota', 'ford']
car = "KIA"
car_0 = "audi"
car_1 = "BMW"
# Checking for conditional tests.

# Checking for inequality "!=".
# (False output)
print(f"Is {car_0.title()} != {cars[0].title()}? I predict True.")
print(car_0 != cars[0])
# (True output)
print(f"\nIs {car_1} != {cars[0].title()}? I predict True.")
print(car_1 != cars[0])


# Checking for equality "==".
# (True output)
print(f"\nIs {car_0.title()} == {cars[0].title()}? I predict True.")
print(car_0 == cars[0])
# (False output)
print(f"\nIs {car_0.title()} == {cars[2].title()}? I predict True.")
print(car_0 == cars[2])

# Checking using lower() method
# (True output)
print(f"\nIs {car_1.lower()} == {cars[1]}? I predict True.")
print(car_1.lower() == cars[1])
# (False output)
print(f"\nIs {car_1} == {cars[1]}? I predict True.")
print(car_1 == cars[1])

# Numerical testing using equality and inequality
# (True output)
print(f"\nIs length of {car_1} == length of {cars[1].upper()}? I predict True.")
print(len(car_1) == len(cars[1]))
# (False output)
print(f"\nIs length of {car_1} == length of {cars[0].title()}? I predict False.")
print(len(car_1) == len(cars[0]))

# Numerical testing using greater than.
# (True output)
print(f"\nIs length of {car_0.title()} > length of {cars[0].title()}? I predict True.")
print(len(car_0) > len(cars[1]))
# (False output)
print(f"\nIs length of {car_1} > length of {cars[1].upper()}? I predict False.")
print(len(car_1) > len(cars[1]))

# Numerical testing using less than.
# (True output)
print(f"\nIs length of {car_1} < length of {car_0.title()}? I predict True.")
print(len(car_1) < len(car_0))
# (False output)
print(f"\nIs length of {car_0.title()} < length of {cars[1]}? I predict False.")
print(len(car_0) < len(cars[1]))

# Numerical testing using less than or equal.
# (True output)
print(f"\nIs length of {cars[1].upper()} <= length of {cars[1]}? I predict True.")
print(len(cars[1]) <= len(cars[1]))
# (False output)
print(f"\nIs length of {car_0.title()} <= length of {car}? I predict False.")
print(len(car_0) <= len(car))

# Using "AND" keyword with "IN".
# (True output)
print(f"\nIs {car_0.title()} and {car_1} in cars list? I predict True.")
print((car_0 and car_1.lower()) in  cars) 
# (False output)
print(f"\nIs {car_0.title()} and {car} in cars list? I predict True.")
print((car_0 and car.lower()) in  cars) 

# Using "OR" keyword with "IN".
# (True output)
print(f"\nIs {car_0.title()} or {car_1} in cars list? I predict True.")
print((car_0 or car_1.lower()) in  cars) 
# (False output)
print(f"\nIs Ferrari or {car} in cars list? I predict False.")
print(("ferrari" or car.lower()) in  cars)

# Using "AND" or "OR" keyword with "NOT IN".
# (True output)
print(f"\nIs Ferrari or {car} in cars list? I predict True.")
print(("ferrari" and car.lower()) not in  cars)
# (False output)
print(f"\nIs {car_0.title()} or {car_1} in cars list? I predict False.")
print((car_0 or car_1.lower()) not in  cars) 