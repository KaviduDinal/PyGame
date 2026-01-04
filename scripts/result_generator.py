# -------------------------------
# Simple Student Result Generator
# -------------------------------

print("===== STUDENT RESULT GENERATOR =====")

# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Number of subjects
num_subjects = int(input("Enter number of subjects: "))

marks = []
total = 0

# Input marks
for i in range(1, num_subjects + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
    total += mark

# Calculations
average = total / num_subjects

# Grade logic
if average >= 75:
    grade = "A"
elif average >= 65:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 35:
    grade = "S"
else:
    grade = "F"

# Pass / Fail
result = "PASS" if average >= 35 else "FAIL"

# Output
print("\n===== RESULT SHEET =====")
print(f"Name       : {name}")
print(f"Roll No    : {roll_no}")
print(f"Total      : {total}")
print(f"Average    : {average:.2f}")
print(f"Grade      : {grade}")
print(f"Result     : {result}")
print("========================")
