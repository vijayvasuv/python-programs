students = [
    {'name': 'Alice', 'height': 165},
    {'name': 'Bob', 'height': 178},
    {'name': 'Charlie', 'height': 155},
    {'name': 'David', 'height': 178},
    {'name': 'Eve', 'height': 165},
]

sorted_students = sorted(students, key = lambda student : student["height"], reverse = True)

for student in sorted_students:
    print(f"Name: {student['name']}, Height: {student['height']}")
