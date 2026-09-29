
print(" STUDENT MARKS ANALYZER ")

students = []

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return (sum(marks) / (len(marks) * 100)) * 100

def calculate_highest(marks):
    return max(marks)

def calculate_lowest(marks):
    return min(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(marks):
    percentage = calculate_percentage(marks)

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def calculate_result(marks):
    percentage = calculate_percentage(marks)

    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"

def add_student():
    name = input("Enter student name: ")
    subjects = int(input("Enter number of subjects: "))

    marks = []

    for i in range(1, subjects + 1):
        mark = int(input(f"Enter marks for subject {i}: "))

        while mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            mark = int(input(f"Enter marks for subject {i}: "))

        marks.append(mark)

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("ALL STUDENTS")

    for student in students:

        marks = student["marks"]
        print("Name:", student["name"])
        print("Marks:", marks)
        print("Total:", calculate_total(marks))
        print("Percentage:", round(calculate_percentage(marks), 2), "%")
        print("Highest:", calculate_highest(marks))
        print("Lowest:", calculate_lowest(marks))
        print("Average:", round(calculate_average(marks), 2))
        print("Grade:", calculate_grade(marks))
        print("Result:", calculate_result(marks))


def search_student():
    name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            marks = student["marks"]
            print("===== STUDENT REPORT =====")
            print("Name:", student["name"])
            print("Marks:", marks)
            print("Total:", calculate_total(marks))
            print("Percentage:", round(calculate_percentage(marks), 2), "%")
            print("Highest:", calculate_highest(marks))
            print("Lowest:", calculate_lowest(marks))
            print("Average:", round(calculate_average(marks), 2))
            print("Grade:", calculate_grade(marks))
            print("Result:", calculate_result(marks))
            found = True
            break

    if not found:
        print("Student not found.")

def highest_scorer():
    if len(students) == 0:
        print("No students found.")
        return
    
    highest_student = students[0]

    for student in students:
        if calculate_percentage(student["marks"]) > calculate_percentage(highest_student["marks"]):
            highest_student = student

    print("HIGHEST SCORER")
    print("Name:", highest_student["name"])
    print(
        "Percentage:",
        round(calculate_percentage(highest_student["marks"]), 2),
        "%"
    )


while True:

    print("MENU")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Find Highest Scorer")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        highest_scorer()

    elif choice == "5":
        print("Thank you for using Student Marks Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")