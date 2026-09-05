"""
Student Result Analyzer

A program to analyze class results: grades, averages,
highest/lowest scorer, and pass/fail statistics.
"""


def get_student_data():
    """
    Ask the teacher how many students there are, then collect
    each student's name and marks.
    Returns a list of dictionaries: [{"name": ..., "marks": ...}, ...]
    """
    students = []

    num_students = int(input("Enter number of students: "))

    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        students.append({"name": name, "marks": marks})

    return students


def main():
    print("=" * 50)
    print("STUDENT RESULT ANALYZER".center(50))
    print("=" * 50)

    students = get_student_data()

    print("\nStudents entered so far:")
    for student in students:
        print(student)


if __name__ == "__main__":
    main()