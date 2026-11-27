prices = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40
}

cart = []

# Collect items until user types 'done'
while True:
    item = input("Enter item name (or 'done' to finish): ").strip().lower()
    if item == "done":
        break
    try:
        if item not in prices:
            raise ValueError("Item not available in store.")
        cart.append(item)
    except ValueError as e:
        print("Error:", e)

# Deduplicate items using a set and calculate total cost
unique_items = set(cart)
total_cost = 0
for item in unique_items:
    if item in prices:
        total_cost += prices[item]

print("Unique items in cart:", unique_items)
print("Total cost:", total_cost)