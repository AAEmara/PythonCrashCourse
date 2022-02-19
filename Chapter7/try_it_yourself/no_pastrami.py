# Storing sandwich names in a list.
sandwich_orders = ["chicken burger", "beef burger", "pastrami",
                    "chicken shawerma", "beef shawerma", "pastrami",
                    "kabab", "falafel", "pastrami",]
finished_orders = []

print("Deli has run out of pastrami.")
# Since the deli has run out of pastrami we have to remove all of the pastrami
# sanwich orders in the list.
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    finished_orders.append(sandwich)

print("\n--- Sandwich Report ---")
i = 0
for sandwich in finished_orders:
    i += 1
    print(f"{i}-) {sandwich.title()}")