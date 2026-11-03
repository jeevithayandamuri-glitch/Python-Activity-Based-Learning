# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic pay: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

# Validate inputs
if (basic < 0 or allowances < 0 or
    overtime_hours < 0 or overtime_rate < 0 or
    incentives < 0):

    print("Invalid Input! Salary values cannot be negative.")

else:

    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = basic + allowances + overtime_pay + incentives

    # Progressive deductions
    if gross_salary <= 10000:
        deduction = 0

    elif gross_salary <= 20000:
        deduction = (gross_salary - 10000) * 0.05

    elif gross_salary <= 40000:
        deduction = (10000 * 0.05) + (
            (gross_salary - 20000) * 0.10
        )

    else:
        deduction = (
            (10000 * 0.05) +
            (20000 * 0.10) +
            ((gross_salary - 40000) * 0.15)
        )

    # Calculate net salary
    net_salary = gross_salary - deduction

    # Display salary statement
    print("\n========== SALARY STATEMENT ==========")

    print("Employee Name       :", name)
    print("Employee ID         :", emp_id)

    print("--------------------------------------")

    print("Basic Pay           : Rs.", round(basic, 2))
    print("Allowances          : Rs.", round(allowances, 2))
    print("Overtime Pay        : Rs.", round(overtime_pay, 2))
    print("Incentives          : Rs.", round(incentives, 2))

    print("--------------------------------------")

    print("Gross Salary        : Rs.", round(gross_salary, 2))
    print("Total Deductions    : Rs.", round(deduction, 2))

    print("--------------------------------------")

    print("Net Salary          : Rs.", round(net_salary, 2))

    print("======================================")
    print("Payroll Generated Successfully!")
