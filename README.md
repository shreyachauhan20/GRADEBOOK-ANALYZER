
📘 GradeBook Analyzer

A simple Python program to input student marks, calculate statistics, assign grades, filter pass/fail, and display results in a formatted table.

📑 Project Description

GradeBook Analyzer is a menu-driven Python application that helps teachers and students quickly analyze class test scores.
Instead of calculating manually, the program automatically computes:

Average

Median

Maximum score

Minimum score

Letter Grades (A–F)

Pass/Fail lists

A formatted results table


This project demonstrates Python fundamentals, including functions, dictionaries, loops, conditionals, list comprehensions, and formatted output.


---

🎯 Features

✔ Manual Student Entry

Enter multiple students and their marks (0-100) manually.

✔ Statistical Analysis

Automatically computes:

Average score

Median score

Highest score

Lowest score


✔ Grade Assignment

Grades assigned based on marks:

Marks	Grade

90–100	A
80–89	B
70–79	C
60–69	D
Below 60	F


✔ Pass/Fail Filter

Uses list comprehension

Passing score = 40


✔ Results Table

A clean, formatted table displaying:

🖥 Tech Used

Dictionaries

Functions

List Comprehensions

F-Strings

Loops & Conditionals


📸 Sample Output
=====================================
      Welcome to GradeBook Analyzer
=====================================

Menu:
1. Enter Student Data
2. Show Statistics
3. Show Grades
4. Show Pass/Fail
5. Show Results Table
6. Exit

Enter your choice: 1
How many students? 5
Enter student name: Alice
Enter marks: 78
Enter student name: Bob
Enter marks: 92
Enter student name: Carol
Enter marks: 56
Enter student name: Tik
Enter marks: 67
Enter student name: Tom
Enter marks: 89

Data stored successfully!

Menu:
1. Enter Student Data
2. Show Statistics
3. Show Grades
4. Show Pass/Fail
5. Show Results Table
6. Exit

Enter your choice: 2

Average: 76.4
Median: 78
Highest Score: 92
Lowest Score: 56

Menu:
1. Enter Student Data
2. Show Statistics
3. Show Grades
4. Show Pass/Fail
5. Show Results Table
6. Exit

Enter your choice: 3

Grades Assigned:
Alice : C
Bob : A
Carol : F
Tik : D
Tom : B

Menu:
1. Enter Student Data
2. Show Statistics
3. Show Grades
4. Show Pass/Fail
5. Show Results Table
6. Exit

Enter your choice: 4

Passed Students: ['Alice', 'Bob', 'Carol', 'Tik', 'Tom'] (5)
Failed Students: [] (0)

Menu:
1. Enter Student Data
2. Show Statistics
3. Show Grades
4. Show Pass/Fail
5. Show Results Table
6. Exit

Enter your choice: 5

----------------------------------------
Name           Marks     Grade
----------------------------------------
Alice          78        C
Bob            92        A
Carol          56        F
Tik            67        D
Tom            89        B
----------------------------------------

Menu:
1. Enter Student Data
2. Show Statistics
3. Show Grades
4. Show Pass/Fail
5. Show Results Table
6. Exit

Enter your choice: 6     

Exiting program... Goodbye!


✨ Learning Outcomes

By completing this project, I_ understand:

Data storage using Python dictionaries

Statistical analysis

Grade computation logic

Working with user input loops

Creating formatted tables
