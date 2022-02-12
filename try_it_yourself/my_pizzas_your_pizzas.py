fav_pizzas = ['chicken pizza', 'margrita', 'cheesy pizza']
friend_pizzas = fav_pizzas[:]

# Adding a new pizza to my list.
fav_pizzas.append("pineapple")
# Adding a new pizza to my friend's list
friend_pizzas.append("pepperoni")

# Talking about my pizzas.
print("My favorite pizzas are:")
for pizza in fav_pizzas:
	print(pizza.title())

# Adding a space between topics.
print("\n")

# Talking about friend's pizzas.
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())