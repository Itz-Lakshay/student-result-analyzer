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


def display_raw_data(students):
    """
    Print the collected student data in a simple, readable form.
    This is just for verifying input at this stage of development —
    the final formatted report comes in a later commit.
    """
    print("\nStudents entered:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, Marks: {student['marks']}")


def main():
    print("=" * 50)
    print("STUDENT RESULT ANALYZER".center(50))
    print("=" * 50)

    students = get_student_data()
    display_raw_data(students)


if __name__ == "__main__":
    main()