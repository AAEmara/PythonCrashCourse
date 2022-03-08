from random import choice
# My list of numbers and letters.
my_list = [1, 2, 0, 's', 4222, 3, 55, 'n',71, 'a',111, 'k', 43, 'e', 18]

# Initiating the lottery_ser variable before saving the lottery serial inside
# it.
lottery_ser = ''
for i in range(4):
    lottery_ser += f"{choice(my_list)}"

print(f"\nThe ticket matching the serial number {lottery_ser} has won the prize!")