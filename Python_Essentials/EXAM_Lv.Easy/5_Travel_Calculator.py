accommodation = float(input("Accommodation: "))
transport = float(input("Transport: "))
food = float(input("Food: "))
people = int(input("People: "))

if people > 0:
    total = accommodation + transport + food
    cost_per_person = total / people

    print()
    print(f"Total Budget: {total:.0f} THB")
    print(f"Cost per Person: {cost_per_person:.2f} THB")
else:
    print("Error: People must be greater than 0")
