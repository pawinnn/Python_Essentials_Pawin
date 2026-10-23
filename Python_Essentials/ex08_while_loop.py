'''
i = 1

while i <= 5:
    print("Hello Python", i)
    i += 1
'''

############
'''

password = ""

while password != "1234":
    password = input("Enter password: ")

print("Login Successful!")

'''
############

while True:
    password = input("Enter password: ")

    if password == "1234":
        print("Login Successful!")
        break

    print("Wrong password. Try again!")