"""
Student Result Analyzer

A program to analyze class results: grades, averages,
highest/lowest scorer, and pass/fail statistics.
"""


def get_student_data():
    """
    Ask the teacher how many students there are, then collect
    each student's name and marks.

    Data structure used:
        students = [
            {"name": "Aman", "marks": 87},
            {"name": "Riya", "marks": 74},
            ...
        ]

    Returns:
        list of dict: one dictionary per student.
    """
    students = []

    num_students = int(input("Enter number of students: "))

    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        students.append({"name": name, "marks": marks})

    return students


def calculate_grade(marks):
    """
    Convert numeric marks into a letter grade.

    Grading scale:
        90-100 -> A+
        80-89  -> A
        70-79  -> B
        60-69  -> C
        50-59  -> D
        0-49   -> F

    Args:
        marks (float): marks scored by a student (0-100).

    Returns:
        str: the letter grade.
    """
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def assign_grades(students):
    """
    Add a 'grade' key to every student dictionary based on their marks.

    Args:
        students (list of dict): student records with 'name' and 'marks'.

    Returns:
        list of dict: same students, each now including a 'grade' key.
    """
    for student in students:
        student["grade"] = calculate_grade(student["marks"])
    return students


def display_raw_data(students):
    """
    Print the collected student data, including grade, in a simple,
    readable form. The final formatted table comes in a later commit.
    """
    print("\nStudents entered:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, "
              f"Marks: {student['marks']}, Grade: {student['grade']}")


def main():
    print("=" * 50)
    print("STUDENT RESULT ANALYZER".center(50))
    print("=" * 50)

    students = get_student_data()
    students = assign_grades(students)
    display_raw_data(students)


if __name__ == "__main__":
    main()