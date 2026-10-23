n = int(input("Enter N: "))

if n > 0:
    total = 0

    print()

    for i in range(1, n + 1):
        total += i
        print(i, end=" + " if i < n else "\n")

    print(f"Total: {total}")

else:
    print("Invalid Number")



'''
#ใช้ while 

n = int(input("Enter N: "))

if n > 0:
    total = 0
    i = 1

    print()

    while i <= n:
        total += i
        print(i, end=" + " if i < n else "\n")
        i += 1

    print(f"Total: {total}")
else:
    print("Invalid Number")
'''