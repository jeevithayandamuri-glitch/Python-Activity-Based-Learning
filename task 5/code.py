
print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")

data_needed = float(input("Enter required data (GB): "))
calls_needed = int(input("Enter required call minutes: "))
sms_needed = int(input("Enter required SMS count: "))
validity_needed = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget (Rs.): "))

n = int(input("\nEnter number of mobile plans: "))

plans = []
eligible_plans = []

if (data_needed < 0 or calls_needed < 0 or
    sms_needed < 0 or validity_needed < 0 or
    budget < 0 or n <= 0):

    print("Invalid input! Please enter valid values.")

else:

    for i in range(n):

        print("\nEnter details for Plan", i + 1)

        price = float(input("Plan price: Rs. "))
        data = float(input("Included data (GB): "))
        calls = int(input("Included call minutes: "))
        sms = int(input("Included SMS: "))
        validity = int(input("Validity in days: "))

        if (price < 0 or data < 0 or calls < 0 or
            sms < 0 or validity < 0):

            print("Invalid plan details. Plan skipped.")
            continue

        extra_data = max(0, data_needed - data)
        extra_calls = max(0, calls_needed - calls)
        extra_sms = max(0, sms_needed - sms)

        data_charge = extra_data * 10
        call_charge = extra_calls * 0.50
        sms_charge = extra_sms * 1

        excess_charge = (
            data_charge + call_charge + sms_charge
        )

        total_cost = price + excess_charge

        eligible = (
            data >= data_needed and
            calls >= calls_needed and
            sms >= sms_needed and
            validity >= validity_needed and
            total_cost <= budget
        )

        plan = {
            "name": "Plan " + str(i + 1),
            "price": price,
            "excess": excess_charge,
            "total": total_cost,
            "eligible": eligible
        }

        plans.append(plan)

        if eligible:
            eligible_plans.append(plan)

        print("Excess Charges: Rs.", round(excess_charge, 2))
        print("Total Cost: Rs.", round(total_cost, 2))
        print("Eligible:", "Yes" if eligible else "No")


    print("\n===== PLAN COMPARISON =====")

    for plan in plans:
        print(
            plan["name"],
            "- Total Cost: Rs.",
            round(plan["total"], 2),
            "- Eligible:", plan["eligible"]
        )

    if eligible_plans:

        best_plan = min(
            eligible_plans,
            key=lambda x: x["total"]
        )

        print("\n===== BEST MOBILE PLAN =====")
        print("Plan Name:", best_plan["name"])
        print("Plan Price: Rs.", best_plan["price"])
        print("Excess Charges: Rs.", best_plan["excess"])
        print("Total Cost: Rs.", round(best_plan["total"], 2))
        print("Status: Most Economical Eligible Plan")

    else:
        print("\nNo eligible plan found within your budget.")

print("\nProgram Completed.")
