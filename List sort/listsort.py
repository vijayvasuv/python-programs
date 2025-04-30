students = [["John", 65], ["Mark", 56], ["Henry", 90], ["Anto", 90]]

sorted_marks = sorted(list(set(student[1] for student in students)), reverse = True)
highest_mark = sorted_marks[0]

sorted_names = sorted(list(set(student[0] for student in students if student[1] == highest_mark)))

print(f"Highest mark: {highest_mark}")
print("Student name(s): ")
for name in sorted_names:
    print(name)
