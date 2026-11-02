
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []
eligible_students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate percentage: "))

    subjects = []
    for j in range(3):
        marks = float(input(f"Enter marks in subject {j + 1}: "))
        subjects.append(marks)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = {
        "name": name,
        "aggregate": aggregate,
        "subjects": subjects,
        "attendance": attendance,
        "income": income,
        "total": sum(subjects)
    }

    students.append(student)

    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subjects) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append(student)

eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        -x["total"],
        x["income"]
    )
)

print("\n===== SCHOLARSHIP RESULTS =====")

if eligible_students:
    print("\nEligible Students Ranking:")

    for rank, student in enumerate(eligible_students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"], "%")
        print("Attendance:", student["attendance"], "%")
        print("Total Subject Marks:", student["total"])
        print("Family Income: Rs.", student["income"])

else:
    print("No eligible students found.")

print("\n===== NOT ELIGIBLE STUDENTS =====")

for student in students:
    if student not in eligible_students:
        print(student["name"])

print("\nProgram Completed.")

