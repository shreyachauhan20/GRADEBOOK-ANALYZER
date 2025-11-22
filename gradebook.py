# ---------------------------------------------------------
# GradeBook Analyzer
# Name: Your Name
# Date: 2025
# Description: Program to input student marks, calculate
# statistics, assign grades, filter pass/fail, and display
# results in a formatted table.
# ---------------------------------------------------------

import statistics

# ---------------------------
# Task 3: Statistical Functions
# ---------------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


# ---------------------------
# Task 4: Grade Assignment
# ---------------------------

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades


# ---------------------------
# Task 5: Pass/Fail Filter
# ---------------------------

def pass_fail_filter(marks_dict):
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    return passed_students, failed_students


# ---------------------------
# Task 6: Results Table
# ---------------------------

def print_results_table(marks_dict, grades_dict):
    print("\n----------------------------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade'}")
    print("----------------------------------------")

    for name, mark in marks_dict.items():
        print(f"{name:<15}{mark:<10}{grades_dict[name]}")

    print("----------------------------------------")


# ---------------------------
# Task 1 & 2: Main Program Loop
# ---------------------------

def main():
    print("=====================================")
    print("      Welcome to GradeBook Analyzer")
    print("=====================================")

    while True:
        print("\nMenu:")
        print("1. Enter Student Data")
        print("2. Show Statistics")
        print("3. Show Grades")
        print("4. Show Pass/Fail")
        print("5. Show Results Table")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            marks = {}
            n = int(input("How many students? "))

            for _ in range(n):
                name = input("Enter student name: ")
                mark = int(input("Enter marks: "))
                marks[name] = mark

            print("\nData stored successfully!")

        elif choice == "2":
            if not marks:
                print("Enter data first!")
                continue

            print("\nAverage:", calculate_average(marks))
            print("Median:", calculate_median(marks))
            print("Highest Score:", find_max_score(marks))
            print("Lowest Score:", find_min_score(marks))

        elif choice == "3":
            if not marks:
                print("Enter data first!")
                continue

            grades = assign_grades(marks)
            print("\nGrades Assigned:")
            for name, g in grades.items():
                print(name, ":", g)

        elif choice == "4":
            if not marks:
                print("Enter data first!")
                continue

            passed, failed = pass_fail_filter(marks)

            print("\nPassed Students:", passed, f"({len(passed)})")
            print("Failed Students:", failed, f"({len(failed)})")

        elif choice == "5":
            if not marks:
                print("Enter data first!")
                continue

            grades = assign_grades(marks)
            print_results_table(marks, grades)

        elif choice == "6":
            print("\nExiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# Run program
if __name__ == "__main__":
    main()
