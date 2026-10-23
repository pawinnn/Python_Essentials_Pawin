
'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")
'''


age = int(input("Enter your age: "))
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted")
else:
    print("Access denied")