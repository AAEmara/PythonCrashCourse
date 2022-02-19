# Storing sandwich names in a list.
sandwich_orders = ["chicken burger", "beef burger", "chicken shawerma",
                    "beef shawerma", "kabab", "falafel",]
finished_sandwiches = []

# Looping through sandwich orders.
for sandwich in sandwich_orders:
    print(f"\nI made your {sandwich.title()} sandwich.")

    # Adding finished sandwiches in the empty list.
    finished_sandwiches.append(sandwich)

# Printing a final report about sandwiches.
print("\n--- Sandwiches Report ---")
i = 0
for sandwich in finished_sandwiches:
    i += 1
    print(f"{i}-) {sandwich.title()}")