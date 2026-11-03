# Multi-Currency Travel Budget Analysis

print("===== TRAVEL BUDGET ANALYSIS =====")

budget = float(input("Enter travel budget in INR: Rs. "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0

if budget < 0 or n <= 0:

    print("Invalid input! Enter valid budget and categories.")

else:

    for i in range(n):

        print("\nExpense Category", i + 1)

        category = input("Enter category name: ")

        amount = float(input("Enter expense amount: "))

        currency = input("Enter currency code: ").upper()

        rate = float(input("Enter exchange rate to INR: "))

        fee_rate = float(input("Enter conversion fee percentage: "))

        # Validate inputs
        if (amount < 0 or rate <= 0 or
                fee_rate < 0 or fee_rate > 100):

            print("Invalid expense details!")
            continue

        # Convert currency into INR
        converted_amount = amount * rate

        # Calculate conversion fee
        conversion_fee = converted_amount * fee_rate / 100

        # Calculate total expense
        total = converted_amount + conversion_fee

        total_spending += total

        expenses.append({
            "category": category,
            "currency": currency,
            "amount": amount,
            "converted": converted_amount,
            "fee": conversion_fee,
            "total": total
        })

    # Calculate remaining budget
    remaining_budget = budget - total_spending

    # Find largest expense category
    if expenses:

        largest = max(expenses, key=lambda x: x["total"])

        # Display report
        print("\n===== TRAVEL EXPENSE REPORT =====")

        print(
            f"{'Category':15} {'Currency':10} "
            f"{'Converted':12} {'Fee':10} {'Total':12}"
        )

        print("-" * 65)

        for e in expenses:

            print(
                f"{e['category']:15} "
                f"{e['currency']:10} "
                f"{e['converted']:12.2f} "
                f"{e['fee']:10.2f} "
                f"{e['total']:12.2f}"
            )

        print("-" * 65)

        print("Travel Budget: Rs.", round(budget, 2))

        print("Total Spending: Rs.",
              round(total_spending, 2))

        print("Largest Expense Category:",
              largest["category"])

        if remaining_budget >= 0:

            print("Remaining Budget: Rs.",
                  round(remaining_budget, 2))

            print("Status: Within Budget")

        else:

            print("Budget Exceeded By: Rs.",
                  round(abs(remaining_budget), 2))

            print("Status: Budget Exceeded")

    else:

        print("No valid expenses entered.")

print("\nTravel Budget Analysis Completed!")
