
#SHREYA CHAUHAN
#GRADEBOOK Analyzer
#10 november 2025
print("""\n--- Welcome to the Simple Gradebook Analyzer!
    This program helps you analyze student marks.
    \n\t\t  --- Main Menu ---\n
    \t1. Enter student grades manually\n
    \t2. Analyze and Display Results\n
    \t3. Exit""")
def choice():
    while True:#Gets a correct menu choice from the user
        choice = input("Please choose an option (1, 2, or 3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please enter the options given")
def get_manual_grades():#Allows manual entry of student names and marks.
    marks = {}
    print("""\n \tManual Grade Entry
    Enter student names and marks. Type 'finished' for name to finish.""")  # <- matched to 'finished'

    while True:
        name = input("Enter student name ,when finished enter 'finished' ").strip()
        if name.lower() == 'finished':
            break

        if not name:
            print("Please enter something")
            continue

        while True:
            try:
                marks_str = input(f"Enter mark for {name} (0-100): ")
                mark = int(marks_str)

                if 0 <= mark <= 100:
                    marks[name] = mark
                    break
                else:
                    print("Mark must be between 0 and 100.")
            except ValueError:
                print("Invalid input,enter a correct number")
    return marks
def check(marks):
    if not marks:
        print("\nNo student data to analyze.")
        return {}
def calculate_avg(marks): # To find Average Score
    mark_list = list(marks.values())
    students = len(mark_list)
    if students == 0:
        print("Total students: 0")
        print("Average score: N/A")
        return
    average = sum(mark_list) / students
    print(f"Total students: {students}")
    print(f"Average score: {average:.2f}")
def calculate_median(mark_list,students):# To find Median Score
    sorted_marks = sorted(mark_list)
    mid = students // 2
    if students % 2 == 0:
        median = (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        median = float(sorted_marks[mid])
    print(f"Median score: {median:.2f}")
def find_max_score(marks):
    if not marks:
        print("Maximum score: N/A")
        return
    max_score = max(marks.values())   # <- use values
    print(f"Maximum score: {max_score}")

def find_min_score(marks):
    if not marks:
        print("Minimum score: N/A")
        return
    min_score = min(marks.values())   # <- use values
    print(f"Minimum score: {min_score}")
    # Function to assign grade based on marks
def get_grade(marks):  # <- single parameter (score)
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def grade_counter(marks,students):
    # Dictionary to store the grades
    grades = {}

    # Assign grades to each student
    for students, mark in marks.items():
        grades[students] = get_grade(mark)  # <- matches new signature

    print("Grades:", grades)

    # Count how many in each grade
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for grade in grades.values():
        grade_count[grade] += 1

    print("Grade Count:", grade_count)
    return grades 
def seperator(marks,grades):
    passing_score = 40
    passed_students = [name for name, mark in marks.items() if mark >= passing_score]
    failed_students = [name for name, mark in marks.items() if mark < passing_score]

    print(f"\n--- Pass/Fail Summary (Passing score: {passing_score}) ---")
    print(f"Passed students ({len(passed_students)}): {', '.join(sorted(passed_students)) if passed_students else 'None'}")
    print(f"Failed students ({len(failed_students)}): {', '.join(sorted(failed_students)) if failed_students else 'None'}")

    return grades # Return the grades for the table
def result_table(marks,grades):
     print("\n--- Detailed Student Results Table ---")
     if not marks:
         print("No student data to display in the table.")
         return

     max_name_len = max(len("Name"), *(len(name) for name in marks.keys()))
     mark_col_width = max(len("Marks"), 3)
     grade_col_width = max(len("Grade"), 1)

     header_line = f"{{:<{max_name_len}}} {{:>{mark_col_width}}} {{:>{grade_col_width}}}"
     print(header_line.format("Name", "Marks", "Grade"))
     print("-" * (max_name_len + mark_col_width + grade_col_width + 6))
     for name in sorted(marks.keys()):
        mark = marks[name]
        grade = grades.get(name, 'N/A')
        print(header_line.format(name, mark, grade))
     print("-" * (max_name_len + mark_col_width + grade_col_width + 6))
def main():
    while True:  # whole program loop
        marks = {}   # stores all student marks

        while True:
            user_choice = choice()   # get menu choice

            if user_choice == '1':
                # enter marks manually
                marks = get_manual_grades()

            elif user_choice == '2':
                # analyze results
                if not marks:
                    print("\nNo student data to analyze.")
                    continue

                mark_list = list(marks.values())
                students = len(mark_list)

                print("\n--- Analysis Results ---")
                calculate_avg(marks)
                calculate_median(mark_list, students)
                find_max_score(marks)
                find_min_score(marks)

                grades = grade_counter(marks, students)
                grades = seperator(marks, grades)
                result_table(marks, grades)

            elif user_choice == '3':
                print("Exiting to main program...")
                break   # reruns program


        again = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("Goodbye!")
            break
main()
