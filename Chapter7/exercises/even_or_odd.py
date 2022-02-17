# Saving the input message in number variable.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
# Converting the input into an integer datatype
number = int(number)

# Checking for even or odd inputs by modulo 2.
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")