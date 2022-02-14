# Creating a number list from 1 to 9.
numbers = list(range(1,10))

# Using for loop to run through the list of numbers.
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")