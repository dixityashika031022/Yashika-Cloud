students = {
    "Yashika": 92,
    "Rahul": 85,
    "Aman": 78,
    "Priya": 88
}

highest = max(students, key=students.get)
print("Topper:", highest)
print("Marks:", students[highest])

for name, marks in students.items():
    print(name, "=", marks)
