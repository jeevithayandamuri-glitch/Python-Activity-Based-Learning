# Hospital Billing and Patient Classification

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

category = input(
    "Enter patient category (General/Senior/BPL): "
).lower()

consultation = float(input("Enter consultation charges: Rs. "))
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))

# Validate billing constraints
if age <= 0:
    print("Invalid age!")

elif consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Charges cannot be negative!")

elif category not in ["general", "senior", "bpl"]:
    print("Invalid patient category!")

else:

    # Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Apply conditional concessions
    if category == "senior":
        concession = total_bill * 0.10

    elif category == "bpl":
        concession = total_bill * 0.20

    else:
        concession = 0

    # Calculate final bill
    final_bill = total_bill - concession

    # Patient classification
    if final_bill < 1000:
        classification = "Low Payment"

    elif final_bill <= 5000:
        classification = "Medium Payment"

    else:
        classification = "High Payment"

    # Display bill
    print("\n===== PATIENT BILL DETAILS =====")

    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Patient Category:", category)

    print("Consultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)

    print("Total Bill: Rs.", total_bill)
    print("Concession: Rs.", concession)
    print("Final Payable Amount: Rs.", final_bill)

    print("Patient Classification:", classification)

    print("\nBilling Completed Successfully!")
