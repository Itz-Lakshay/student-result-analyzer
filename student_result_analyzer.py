"""
Student Result Analyzer

A program to analyze class results: grades, averages,
highest/lowest scorer, and pass/fail statistics.
"""

PASSING_MARKS = 50


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
    """
    for student in students:
        student["grade"] = calculate_grade(student["marks"])
    return students


def assign_status(students):
    """
    Add a 'status' key ('PASS' or 'FAIL') to every student dictionary,
    based on the passing marks threshold.
    """
    for student in students:
        student["status"] = "PASS" if student["marks"] >= PASSING_MARKS else "FAIL"
    return students


def calculate_average(students):
    """
    Calculate the average marks of the class, rounded to 2 decimal places.
    """
    total_marks = sum(student["marks"] for student in students)
    average = total_marks / len(students)
    return round(average, 2)


def find_highest_scorer(students):
    """
    Find the student(s) with the highest marks. Handles ties.
    """
    highest_marks = max(student["marks"] for student in students)
    return [student for student in students if student["marks"] == highest_marks]


def find_lowest_scorer(students):
    """
    Find the student(s) with the lowest marks. Handles ties.
    """
    lowest_marks = min(student["marks"] for student in students)
    return [student for student in students if student["marks"] == lowest_marks]


def calculate_pass_fail(students):
    """
    Calculate class-wide pass/fail counts and percentages.

    Returns:
        dict: {
            "passed": int,
            "failed": int,
            "pass_percentage": float,
            "fail_percentage": float
        }
    """
    total = len(students)
    passed = sum(1 for student in students if student["status"] == "PASS")
    failed = total - passed

    pass_percentage = round((passed / total) * 100, 2)
    fail_percentage = round((failed / total) * 100, 2)

    return {
        "passed": passed,
        "failed": failed,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage,
    }


def display_raw_data(students):
    """
    Print the collected student data, including grade and status.
    The final formatted table comes in a later commit.
    """
    print("\nStudents entered:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. Name: {student['name']}, "
              f"Marks: {student['marks']}, Grade: {student['grade']}, "
              f"Status: {student['status']}")


def display_class_statistics(students):
    """
    Print class-level statistics: average, highest/lowest scorer,
    and pass/fail breakdown.
    """
    average = calculate_average(students)
    top_students = find_highest_scorer(students)
    bottom_students = find_lowest_scorer(students)
    pass_fail = calculate_pass_fail(students)

    top_names = ", ".join(s["name"] for s in top_students)
    bottom_names = ", ".join(s["name"] for s in bottom_students)

    print("\n--- Class Statistics ---")
    print(f"Class Average: {average}")
    print(f"Highest Scorer: {top_names} ({top_students[0]['marks']})")
    print(f"Lowest Scorer: {bottom_names} ({bottom_students[0]['marks']})")
    print(f"Passed: {pass_fail['passed']}")
    print(f"Failed: {pass_fail['failed']}")
    print(f"Pass Percentage: {pass_fail['pass_percentage']}%")
    print(f"Fail Percentage: {pass_fail['fail_percentage']}%")


def main():
    print("=" * 50)
    print("STUDENT RESULT ANALYZER".center(50))
    print("=" * 50)

    students = get_student_data()
    students = assign_grades(students)
    students = assign_status(students)
    display_raw_data(students)
    display_class_statistics(students)


if __name__ == "__main__":
    main()