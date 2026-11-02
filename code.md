
## 1. Problem Statement
Develop a Python program to select eligible students for scholarships based on aggregate marks, subject-wise minimum marks, attendance percentage, and family income. Rank eligible students according to their marks.

## 2. Objectives
- To identify scholarship-eligible students.
- To check marks, attendance, and income criteria.
- To rank eligible students based on aggregate marks.
- To display the final scholarship selection list.

## 3. Assumptions
- Minimum aggregate marks: 75%.
- Minimum marks in each subject: 60%.
- Minimum attendance: 75%.
- Maximum annual family income: ₹2,00,000.
- Students who satisfy all conditions are eligible.

## 4. Algorithm
1. Start.
2. Input the student's name, subject marks, attendance, and family income.
3. Calculate the aggregate percentage.
4. Check all eligibility conditions.
5. If all conditions are satisfied, declare the student eligible.
6. Otherwise, declare the student not eligible.
7. Display the aggregate percentage and eligibility result.
8. Stop.

## 5. Flowchart
Start  
↓  
Input student details  
↓  
Calculate aggregate percentage  
↓  
Check marks, attendance, and income  
↓  
Are all conditions satisfied?  
↙ Yes                 ↘ No  
Eligible              Not Eligible  
↘                     ↙  
Display result  
↓  
Stop

## 6. Pseudocode
```
START
INPUT student name
INPUT marks in three subjects
INPUT attendance
INPUT family income

CALCULATE aggregate percentage

IF aggregate >= 75 AND
   every subject mark >= 60 AND
   attendance >= 75 AND
   income <= 200000
    PRINT "Eligible for Scholarship"
ELSE
    PRINT "Not Eligible for Scholarship"
END IF

STOP
```

## 7. Python Source Code
```python
name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

aggregate = (m1 + m2 + m3) / 3

print("\n--- Scholarship Details ---")
print("Student Name:", name)
print("Aggregate Percentage:", round(aggregate, 2))

if (aggregate >= 75 and
    m1 >= 60 and m2 >= 60 and m3 >= 60 and
    attendance >= 75 and income <= 200000):

    print("Result: Eligible for Scholarship")
else:
    print("Result: Not Eligible for Scholarship")
```

## 8. Test Cases

| Student | Marks | Attendance | Annual Income | Result |
|---|---|---|---|---|
| Ravi | 80, 85, 90 | 90% | ₹1,50,000 | Eligible |
| Sita | 50, 80, 85 | 85% | ₹1,00,000 | Not Eligible |
| Kumar | 80, 85, 90 | 60% | ₹1,50,000 | Not Eligible |
| Priya | 80, 85, 90 | 90% | ₹3,00,000 | Not Eligible |

## 9. Sample Output
```
Enter student name: Ravi
Enter marks in Subject 1: 80
Enter marks in Subject 2: 85
Enter marks in Subject 3: 90
Enter attendance percentage: 90
Enter annual family income: 150000

--- Scholarship Details ---
Student Name: Ravi
Aggregate Percentage: 85.0
Result: Eligible for Scholarship
```

## 10. Conclusion
This program checks scholarship eligibility using conditional statements and arithmetic operators. It helps identify students who satisfy the specified academic, attendance, and family income requirements.
