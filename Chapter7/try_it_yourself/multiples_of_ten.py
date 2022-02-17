# Saving the input message in number variable.
number = input(f"Hello, Please enter a number: ")
number = int(number)

# Applying the condition on the number to check wether it was a multiple
# of 10 or not.
if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")