#Dic = {"key" : "value"}

student = {
    "name": "Alice",
    "age": 20,
    "city": "Bangkok",
    "Pet": ["Dog","Cat"]
}

student["new"] = ["Item"]

print(student)
print(student["name"])
print(student["Pet"][0])

print("==============================\n")
#method
student.update({"country":"Thailand"})
print(student)
print(student.keys())
print(student.values())
print(student.get("Pet"))


#Key ช่วยให้เราเข้าใจความหมายของข้อมูลได้ชัดเจนกว่าการอ้างอิงผ่านตำแหน่งเพียงอย่างเดียว

print("==============================\n")

student = {
    "name": "Alice",
    "age": 20,
    "city": "Bangkok",
    "Pet": ["Dog","Cat"]
}

for k, v in student.items():
    print(k, v)

for k in student.keys():
    print(k)

for v in student.values():
    print(v)




print("\n==============================\n")
#ใช้ List ร่วมกับ Dicts

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 90}
]

for student in students:
    print(student["name"], student["score"])


#List ใช้เก็บนักเรียนหลายคน
#Dictionary ใช้เก็บรายละเอียดของนักเรียนแต่ละคน