# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

# Input details
product = input("Enter product name: ")

units = int(input("Enter number of units produced: "))

material = float(input("Enter material cost per unit: Rs. "))

labour = float(input("Enter labour charges per unit: Rs. "))

wastage = float(input("Enter wastage percentage: "))

machine = float(input("Enter machine cost per unit: Rs. "))

selling_price = float(input("Enter selling price per unit: Rs. "))

target = float(input("Enter profit target percentage: "))

# Input validation
if (units <= 0 or material < 0 or labour < 0 or
    wastage < 0 or wastage > 100 or machine < 0 or
    selling_price < 0 or target < 0):

    print("Invalid Input! Please enter valid values.")

else:

    # Calculate material cost
    material_cost = units * material

    # Calculate labour cost
    labour_cost = units * labour

    # Calculate wastage cost
    wastage_cost = (
        (material_cost + labour_cost) * wastage / 100
    )

    # Calculate machine cost
    machine_cost = units * machine

    # Calculate total production cost
    total_cost = (
        material_cost + labour_cost +
        wastage_cost + machine_cost
    )

    # Calculate revenue
    revenue = units * selling_price

    # Calculate profit
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Check profit target
    print("\n===== PROFITABILITY REPORT =====")

    print("Product Name       :", product)
    print("Units Produced     :", units)

    print("-----------------------------------")

    print("Material Cost      : Rs.", round(material_cost, 2))
    print("Labour Cost        : Rs.", round(labour_cost, 2))
    print("Wastage Cost       : Rs.", round(wastage_cost, 2))
    print("Machine Cost       : Rs.", round(machine_cost, 2))

    print("-----------------------------------")

    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Revenue        : Rs.", round(revenue, 2))
    print("Total Profit         : Rs.", round(profit, 2))

    print("Profit Percentage   :", round(profit_percentage, 2), "%")

    print("-----------------------------------")

    if profit_percentage >= target:
        print("Status: Profit Target Achieved!")
    else:
        print("Status: Profit Target Not Achieved!")

    print("Target Profit Percentage:", target, "%")

    print("\nAnalysis Completed Successfully!")
