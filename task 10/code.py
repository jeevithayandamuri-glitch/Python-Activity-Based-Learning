
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transport cost: "))

catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))

sponsorship_target = float(input("Enter sponsorship target: "))
sponsorship_received = float(input("Enter sponsorship received: "))

fixed_cost = venue + equipment + transport
variable_cost = catering + certificate

total_cost = fixed_cost + (variable_cost * participants)

participant_contribution = participants * registration_fee

sponsorship_shortfall = max(
    0, sponsorship_target - sponsorship_received
)

net_cost = fixed_cost - sponsorship_received
contribution_per_person = registration_fee - variable_cost

if net_cost <= 0:
    break_even = 0
elif contribution_per_person <= 0:
    break_even = None
else:
    break_even = math.ceil(net_cost / contribution_per_person)

total_income = participant_contribution + sponsorship_received
balance = total_income - total_cost

print("\n------ CAMPUS EVENT FINANCIAL REPORT ------")
print("Fixed Cost:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Event Cost:", total_cost)
print("Participant Contributions:", participant_contribution)
print("Sponsorship Received:", sponsorship_received)
print("Sponsorship Shortfall:", sponsorship_shortfall)

if break_even is None:
    print("Break-even: Not possible at the given registration fee")
else:
    print("Minimum Registrations for Break-even:", break_even)

if balance > 0:
    print("Financial Result: Surplus of", balance)
elif balance < 0:
    print("Financial Result: Deficit of", abs(balance))
else:
    print("Financial Result: Break-even")
