# Railway Fare and Reservation Calculator

print("===== RAILWAY RESERVATION SYSTEM =====")

n = int(input("Enter number of passengers: "))
distance = float(input("Enter travel distance (km): "))

print("\nSelect Travel Class")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")
print("4. AC 1 Tier")

choice = int(input("Enter class choice: "))

# Class rates
if choice == 1:
    travel_class = "Sleeper"
    rate = 1.50

elif choice == 2:
    travel_class = "AC 3 Tier"
    rate = 2.50

elif choice == 3:
    travel_class = "AC 2 Tier"
    rate = 3.50

elif choice == 4:
    travel_class = "AC 1 Tier"
    rate = 5.00

else:
    rate = 0
    travel_class = "Invalid"

# Validate input
if n <= 0 or distance <= 0 or rate == 0:
    print("Invalid booking details!")

else:

    passengers = []
    total_fare = 0

    # Distance-based charge
    if distance <= 100:
        distance_charge = 0

    elif distance <= 300:
        distance_charge = 0.10

    else:
        distance_charge = 0.20

    for i in range(n):

        print("\nPassenger", i + 1)

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))

        if age < 0:
            print("Invalid age!")
            continue

        # Calculate basic fare
        basic_fare = distance * rate

        # Apply distance charge
        basic_fare = basic_fare + (
            basic_fare * distance_charge
        )

        # Age concession
        if age < 5:
            concession = 0
            reservation_fee = 0
            fare = 0

        else:

            if age >= 60:
                concession = basic_fare * 0.10
            else:
                concession = 0

            reservation_fee = 40

            fare = (
                basic_fare
                - concession
                + reservation_fee
            )

        passengers.append({
            "name": name,
            "age": age,
            "fare": fare
        })

        total_fare += fare

        print("Passenger Fare: Rs.", round(fare, 2))

    # Display booking details
    print("\n===== RESERVATION SUMMARY =====")

    print("Travel Class:", travel_class)
    print("Distance:", distance, "km")

    for p in passengers:
        print(
            p["name"],
            "- Age:", p["age"],
            "- Fare: Rs.", round(p["fare"], 2)
        )

    print("Total Reservation Fare: Rs.",
          round(total_fare, 2))

    # Cancellation calculation
    cancel = input(
        "\nDo you want to cancel the reservation? (yes/no): "
    ).lower()

    if cancel == "yes":

        hours = float(input(
            "Enter hours remaining before departure: "
        ))

        if hours < 0:
            print("Invalid cancellation time!")

        else:

            if hours <= 24:
                penalty_rate = 0.25
            else:
                penalty_rate = 0.10

            penalty = total_fare * penalty_rate
            refund = total_fare - penalty

            print("\n===== CANCELLATION DETAILS =====")
            print("Total Fare: Rs.", round(total_fare, 2))
            print("Cancellation Penalty: Rs.",
                  round(penalty, 2))
            print("Refund Amount: Rs.",
                  round(refund, 2))

    elif cancel == "no":
        print("Reservation Confirmed!")

    else:
        print("Invalid cancellation choice!")

print("\nThank You for Using Railway Reservation System!")
