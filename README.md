# Student Result Analyzer

## About
Student Result Analyzer is a command-line Python program built for the
Association of Computer Enthusiasts (ACE) society. It takes a teacher's
class list of student names and marks, and automatically generates a
complete result analysis — grades, class statistics, and a pass/fail
breakdown — with results exportable to TXT, CSV, and PDF.

## Features
- Collects multiple students' names and marks via the terminal
- Full input validation (non-numeric input, out-of-range marks, empty names, invalid counts)
- Grade calculation per student (A+, A, B, C, D, F)
- Class average, highest scorer, and lowest scorer (with tie handling)
- Pass/fail counts and percentages
- Clean, aligned result table printed to the terminal
- Exports results to:
  - `student_results.txt` — plain text report
  - `student_results.csv` — structured student-wise data
  - `student_results.pdf` — styled PDF report, generated with ReportLab

## Technologies
```
Python
CSV (built-in csv module)
File Handling
ReportLab
Git/GitHub
```

## How to Run

1. Clone the repository:
```bash
   git clone https://github.com/<your-username>/student-result-analyzer.git
   cd student-result-analyzer
```
2. Install dependencies:
```bash
   pip install reportlab
```
3. Run the program:
```bash
   python student_result_analyzer.py
```
4. Follow the prompts to enter the number of students, then each student's name and marks.
5. Once complete, the terminal will display the result report, and three files — `student_results.txt`, `student_results.csv`, and `student_results.pdf` — will be generated in the same folder.

## Sample Output

```
==================================================
              STUDENT RESULT ANALYZER
==================================================

Name           Marks     Grade     Status    
---------------------------------------------
Aman           87.0      A         PASS      
Riya           74.0      B         PASS      
Rahul          42.0      F         FAIL      
---------------------------------------------
Class Average: 67.67
Highest Scorer: Aman (87.0)
Lowest Scorer: Rahul (42.0)
Passed: 2
Failed: 1
Pass Percentage: 66.67%
Fail Percentage: 33.33%
==================================================

Report saved to student_results.txt
Report saved to student_results.csv
Report saved to student_results.pdf
```

## Project Structure
```
student-result-analyzer/
│
├── student_result_analyzer.py   # Main program
├── student_results.txt          # Generated on run
├── student_results.csv          # Generated on run
├── student_results.pdf          # Generated on run
├── .gitattributes                # Line-ending / binary file rules
└── README.md
```

## Future Improvements
- Search for a student by name
- Sort and display students by marks
- Support multiple subjects per student
- Menu-driven interface to re-run analysis without restarting the program