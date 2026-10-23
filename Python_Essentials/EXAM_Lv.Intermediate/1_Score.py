score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Result: Invalid Score")
elif score >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")