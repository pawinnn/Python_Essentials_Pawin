name = input("What's your name: ")
print("Hello", name)

#ปกติ input จะคืนค่าออกมาเป็น str เสมอ

#สามารถกำหนดชนิดให้กับ input
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)


#ทศนิยม
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total price:", total)

# f-string จะง่ายต่อการจัดรูปแบบผลลัพธ์
print(f"Total price {total}")

#กำหนดจุดทศนิยม
print(f"Total price: {total:.3f}")