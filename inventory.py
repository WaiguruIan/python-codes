inventory = {}

n = int(input("How many items do you want to add? "))

for i in range(n):
    name = input(f"Enter item name {i+1}: ")
    quantity = int(input(f"Enter quantity {i+1}: "))

    inventory[name] = inventory.get(name, 0) + quantity
    print()

want_search = input("Do you want to search an item? (yes/no): ")
search = want_search == "yes"

if search:
    item = input("Enter item name to search: ")
    print(item, inventory.get(item, "Item not found"))

total = 0
for q in inventory.values():
    total += q

print("Total quantity:", total)
