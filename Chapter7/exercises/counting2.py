current_number = 0

while current_number < 10:
    current_number += 1
    # If the current number is divisible by 2 continue to the beginning of
    # the loop if not continue the rest of the code (print statement).
    if current_number % 2 == 0:
        continue

    print(current_number)