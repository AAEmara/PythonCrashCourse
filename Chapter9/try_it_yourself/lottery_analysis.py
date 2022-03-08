from random import choice
# Trying to win this lottery k42221111.
my_ticket = [1, 2, 0, 's', 4222, 3, 55, 'n',71, 'a',111, 'k', 43, 'e', 18]

lottery_ser = ''
iteration = 0

while lottery_ser != "k42221111":
    # Incrementing the iteration by 1.
    iteration += 1
    # Resetting the lottery serial again.
    lottery_ser = ''
    
    # Creating lottery number through a for loop.
    for i in range(4):
        lottery_ser += f"{choice(my_ticket)}"

print(f"You have taken {iteration} times to win the lottery!")