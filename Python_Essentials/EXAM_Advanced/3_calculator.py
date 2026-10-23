'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("=== CALCULATOR ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("\nChoose: ")

if choice in ["1", "2", "3", "4"]:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)

    print(f"\nResult: {result:g}" if isinstance(result, float) else f"\nResult: {result}")
else:
    print("Invalid Choice")

'''

#Bonus
# Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b


# Main Program

while True:
    print("\n=== CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("0. Exit")

    choice = input("\nChoose: ")

    if choice == "0":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid Choice")
        continue

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    elif choice == "5":
        result = power(num1, num2)
    elif choice == "6":
        result = modulo(num1, num2)

    print(f"\nResult: {result}")