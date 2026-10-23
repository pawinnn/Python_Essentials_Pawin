weight = int(input("your weight (kg):"))
height = int(input("your height (cm):"))

BMI = weight/(height/100)**2
BMI_float = float(BMI)

print(f"Your BMI is: {BMI_float:.2f}")
