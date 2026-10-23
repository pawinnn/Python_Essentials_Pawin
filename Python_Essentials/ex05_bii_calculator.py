product_name = input("Product name: ")
product_price = float(input("Price : "))
product_quantity = int(input("Quantity: "))


total = product_price * product_quantity

print("==========RECEIPT========")
print(f"Product name: {product_name}")
print(f"Price: {product_price} THB/item" )
print(f"Quantity: {product_quantity} items")
print(f"Total : {total:.2f} THB")
