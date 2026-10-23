
inventory = {
    "Apple": 15,
    "Banana": 20,
    "Orange": 10,
    "Mango": 8,
    "Grape": 12
}

product = input("Enter product: ")

if product in inventory:
    print(f"\n{product}: {inventory[product]} items remaining")
else:
    print("\nProduct not found")