import csv

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

"""
Student Result Analyzer

A program to analyze class results: grades, averages,
highest/lowest scorer, and pass/fail statistics.
"""

PASSING_MARKS = 50


def get_valid_number_of_students():
    """
    Repeatedly ask for the number of students until a valid
    positive integer is entered.
    """
    while True:
        raw_value = input("Enter number of students: ")
        try:
            num_students = int(raw_value)
            if num_students <= 0:
                print("Number of students must be a positive whole number. Try again.")
                continue
            return num_students
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_name():
    """
    Repeatedly ask for a student name until a non-empty value is entered.
    """
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be empty. Please try again.")
            continue
        return name


def get_valid_marks():
    """
    Repeatedly ask for marks until a valid number between 0 and 100
    is entered.
    """
    while True:
        raw_value = input("Enter marks: ")
        try:
            marks = float(raw_value)
        except ValueError:
            print("Invalid input. Marks must be numeric. Try again.")
            continue

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100. Try again.")
            continue

        return marks


def get_student_data():
    """
    Ask the teacher how many students there are, then collect
    each student's name and marks, validating every input.
    """
    students = []

    num_students = get_valid_number_of_students()

    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        name = get_valid_name()
        marks = get_valid_marks()

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
    Add a 'status' key ('PASS' or 'FAIL') to every student dictionary.
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


def build_report_lines(students):
    """
    Build the full report as a list of text lines (no printing here).

    This is the key idea behind this commit: the report's *content*
    is generated once, as plain strings, so it can be reused for
    the terminal, the TXT file, and later the PDF — without
    duplicating the formatting logic in three places.

    Returns:
        list of str: each item is one line of the report.
    """
    average = calculate_average(students)
    top_students = find_highest_scorer(students)
    bottom_students = find_lowest_scorer(students)
    pass_fail = calculate_pass_fail(students)

    top_names = ", ".join(s["name"] for s in top_students)
    bottom_names = ", ".join(s["name"] for s in bottom_students)

    lines = []
    lines.append("=" * 50)
    lines.append("STUDENT RESULT ANALYZER".center(50))
    lines.append("=" * 50)
    lines.append("")
    lines.append(f"{'Name':<15}{'Marks':<10}{'Grade':<10}{'Status':<10}")
    lines.append("-" * 45)

    for student in students:
        lines.append(f"{student['name']:<15}{student['marks']:<10}"
                      f"{student['grade']:<10}{student['status']:<10}")

    lines.append("-" * 45)
    lines.append(f"Class Average: {average}")
    lines.append(f"Highest Scorer: {top_names} ({top_students[0]['marks']})")
    lines.append(f"Lowest Scorer: {bottom_names} ({bottom_students[0]['marks']})")
    lines.append(f"Passed: {pass_fail['passed']}")
    lines.append(f"Failed: {pass_fail['failed']}")
    lines.append(f"Pass Percentage: {pass_fail['pass_percentage']}%")
    lines.append(f"Fail Percentage: {pass_fail['fail_percentage']}%")
    lines.append("=" * 50)

    return lines


def display_report(report_lines):
    """
    Print the report lines to the terminal.
    """
    for line in report_lines:
        print(line)


def save_to_txt(report_lines, filename="student_results.txt"):
    """
    Save the report lines to a plain text file.
    """
    with open(filename, "w") as file:
        for line in report_lines:
            file.write(line + "\n")
    print(f"Report saved to {filename}")


def save_to_csv(students, filename="student_results.csv"):
    """
    Save student-wise results to a CSV file.

    Format:
        Name,Marks,Grade,Status
        Aman,87.0,A,PASS
        Riya,74.0,B,PASS
        ...

    Args:
        students (list of dict): student records, each with
            'name', 'marks', 'grade', 'status'.
        filename (str): output file name.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Marks", "Grade", "Status"])

        for student in students:
            writer.writerow([
                student["name"],
                student["marks"],
                student["grade"],
                student["status"],
            ])

    print(f"Report saved to {filename}")


def generate_pdf(students, filename="student_results.pdf"):
    """
    Generate a clean, professional PDF report containing the
    student result table and class statistics.

    Args:
        students (list of dict): student records with name, marks,
            grade, status.
        filename (str): output PDF file name.
    """
    average = calculate_average(students)
    top_students = find_highest_scorer(students)
    bottom_students = find_lowest_scorer(students)
    pass_fail = calculate_pass_fail(students)

    top_names = ", ".join(s["name"] for s in top_students)
    bottom_names = ", ".join(s["name"] for s in bottom_students)

    doc = SimpleDocTemplate(filename, pagesize=A4,
                             topMargin=2 * cm, bottomMargin=2 * cm)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        spaceAfter=20,
    )

    elements = []

    # Title
    elements.append(Paragraph("STUDENT RESULT ANALYZER", title_style))
    elements.append(Spacer(1, 12))

    # Student result table
    table_data = [["Name", "Marks", "Grade", "Status"]]
    for student in students:
        table_data.append([
            student["name"],
            student["marks"],
            student["grade"],
            student["status"],
        ])

    student_table = Table(table_data, colWidths=[6 * cm, 3 * cm, 3 * cm, 3 * cm])
    student_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2C3E50")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(student_table)
    elements.append(Spacer(1, 24))

    # Class statistics
    stats_heading_style = ParagraphStyle(
        "StatsHeading",
        parent=styles["Heading2"],
        spaceAfter=10,
    )
    elements.append(Paragraph("Class Statistics", stats_heading_style))

    stats_lines = [
        f"Class Average: {average}",
        f"Highest Scorer: {top_names} ({top_students[0]['marks']})",
        f"Lowest Scorer: {bottom_names} ({bottom_students[0]['marks']})",
        f"Passed: {pass_fail['passed']}",
        f"Failed: {pass_fail['failed']}",
        f"Pass Percentage: {pass_fail['pass_percentage']}%",
        f"Fail Percentage: {pass_fail['fail_percentage']}%",
    ]

    for line in stats_lines:
        elements.append(Paragraph(line, styles["Normal"]))
        elements.append(Spacer(1, 6))

    doc.build(elements)
    print(f"Report saved to {filename}")


def main():
    students = get_student_data()
    students = assign_grades(students)
    students = assign_status(students)

    report_lines = build_report_lines(students)
    display_report(report_lines)
    save_to_txt(report_lines)
    save_to_csv(students)
    generate_pdf(students)


if __name__ == "__main__":
    main()