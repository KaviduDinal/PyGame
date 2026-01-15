# ============================================
# Student Result Management System
# Single File Python Program
# ============================================

students = []

# --------------------------------------------
# Add student details
# --------------------------------------------
def add_student():
    print("\n➕ Add New Student")
    sid = input("Student ID: ")
    name = input("Student Name: ")

    sub1 = float(input("Marks - Subject 1: "))
    sub2 = float(input("Marks - Subject 2: "))
    sub3 = float(input("Marks - Subject 3: "))

    average = (sub1 + sub2 + sub3) / 3

    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    student = {
        "ID": sid,
        "Name": name,
        "Sub1": sub1,
        "Sub2": sub2,
        "Sub3": sub3,
        "Average": round(average, 2),
        "Grade": grade
    }

    students.append(student)
    print("✅ Student added successfully!")

# --------------------------------------------
# View all students
# --------------------------------------------
def view_students():
    if not students:
        print("\n⚠️ No student records found!")
        return

    print("\n📋 Student List")
    print("-" * 50)
    for s in students:
        print(f"""
ID      : {s['ID']}
Name    : {s['Name']}
Average : {s['Average']}
Grade   : {s['Grade']}
------------------------------
""")

# --------------------------------------------
# Search student
# --------------------------------------------
def search_student():
    sid = input("\nEnter Student ID to search: ")

    for s in students:
        if s["ID"] == sid:
            print("\n🔍 Student Found")
            print(s)
            return

    print("❌ Student not found!")

# --------------------------------------------
# Main menu
# --------------------------------------------
def main():
    while True:
        print("""
====================================
 Student Result Management System
====================================
1. Add Student
2. View All Students
3. Search Student
4. Exit
====================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("\n👋 Exiting program. Thank you!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    main()
