def manage_grocery_list():
    filename = "grocery.txt"
    items = []
    
    print("Enter grocery items (type 'done' when finished):")
    while True:
        item = input("Item: ").strip()
        if item.lower() == 'done':
            break
        if item:
            items.append(item)
            
    # Write items into the file, each on a new line
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
            
    print(f"\nSuccessfully saved {len(items)} items to {filename}.")

# Run the function
manage_grocery_list()