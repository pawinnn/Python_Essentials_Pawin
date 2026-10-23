score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 80:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >= 60:
    print("Your grade is C")
elif score >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")
