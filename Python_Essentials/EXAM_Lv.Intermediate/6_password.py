'''
password = "hello123"

user_password = input("Enter password: ")

print()

if user_password == password:
    print("Access Granted")
else:
    print("Access Denied")
'''


#BONUS

password = "hello123"
attempts = 0

while attempts < 3:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Access Denied")

        if attempts == 3:
            print("Account Locked")