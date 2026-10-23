shopping_list = []

while True:
    item = input("Enter item: ")

    if item.lower() == "done":
        break

    shopping_list.append(item)

print("\nShopping List:")

for i,item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")


#enumerate() คือ ฟังก์ชันที่ใช้สำหรับวนซ้ำ (iterate) ข้อมูลผ่านออบเจ็กต์ที่สามารถวนซ้ำได้เช่น 