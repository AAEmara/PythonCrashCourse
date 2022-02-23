# Definign a function that takes many arguments as items to a sandwich using
# propositional arguments (*args).
def make_sandwich(*items):
    """Summarizes the sandwich that has been ordered."""
    print("\n--- Sandwich Summary Report ---")
    for item in items:
        print(f"- {item}")

# First Sandwich
make_sandwich('bread', 'cheese', 'lettuce', 'beef burger', 'ketchup',)
# Second Sandwich
make_sandwich('bread', 'sausage', 'mustard', 'ketchup')
# Third Sandwich
make_sandwich('bread', 'chicken slices', 'garlic sauce', 'pickels')