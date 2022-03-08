class Die:
    """Simulating a real die"""

    def __init__(self, sides):
        self.sides = 6

    def roll_die(self):
        """
        A method that prints a random number between 1 and the number of
        sides of the die
        """
        from random import randint
        return randint(1,self.sides)

# Initiating instances from Die class.
six_side = Die(6)
ten_side = Die(10)
twenty_side = Die(20)

# Rolling the 6-sided die 10 times.
print(f"--- Printing the {six_side.sides}-sided dice rolling results ---")
for i in range(10):
    print(six_side.roll_die())

# Rolling the 10-sided die 10 times.
print(f"--- Printing the {ten_side.sides}-sided dice rolling results ---")
for i in range(10):
    print(ten_side.roll_die())

# Rolling the 10-sided die 10 times.
print(f"--- Printing the {twenty_side.sides}-sided dice rolling results ---")
for i in range(10):
    print(twenty_side.roll_die())