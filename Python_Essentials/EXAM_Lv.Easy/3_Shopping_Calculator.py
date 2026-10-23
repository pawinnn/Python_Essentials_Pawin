Product = input("Product :")
Price = float(input("Price :"))
Quantity = int(input("Quantity : "))

print()
print("======RECEIPT======")
print(f"{Product} x {Quantity} ")
print(f"Total : {Price*Quantity:.2f} THB")
print("===================")

discount = int(input("Discount :"))

print()
print("======RECEIPT======")
print(f"{Product} x {Quantity} ")
print(f"Discount {discount}%")
print(f"Total : {Price*Quantity*(((100-discount))/100):.2f} THB")
print("===================")