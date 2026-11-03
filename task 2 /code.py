
n = int(input("Enter number of months: "))

bills = []
units_list = []

for i in range(n):

    print("\nMonth", i + 1)

    units = int(input("Enter electricity units consumed: "))

  
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed_charge = 50

    surcharge = energy_charge * 0.05

    if units < 100:
        rebate = energy_charge * 0.05
    else:
        rebate = 0
      
    total = energy_charge + fixed_charge + surcharge - rebate

    bills.append(total)
    units_list.append(units)

    print("Energy Charge: Rs.", energy_charge)
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", surcharge)
    print("Rebate: Rs.", rebate)
    print("Total Bill: Rs.", round(total, 2))


print("\n----- MONTHLY BILL COMPARISON -----")

for i in range(n):

    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            percentage = (increase / bills[i - 1]) * 100

            if percentage > 30:
                print("Warning: Unusual increase detected!")
            else:
                print("Bill is within normal range.")

        else:
            print("Cannot calculate percentage increase.")

print("\nTotal Electricity Expense: Rs.", round(sum(bills), 2))

print("\nProgram Completed.")
