# Retail Billing with Multiple Discount Rules

print("========== RETAIL BILLING SYSTEM ==========")

n = int(input("Enter number of products: "))

products = []
subtotal = 0
total_tax = 0

tax_rates = {
    "electronics": 0.18,
    "clothing": 0.05,
    "groceries": 0.00,
    "furniture": 0.12
}

if n <= 0:
    print("Invalid number of products!")

else:

    for i in range(n):

        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        category = input(
            "Enter category (Electronics/Clothing/Groceries/Furniture): "
        ).lower()

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: Rs. "))

        # Validate product details
        if (quantity <= 0 or price < 0 or
                category not in tax_rates):

            print("Invalid product details!")
            continue

        # Calculate item amount
        amount = quantity * price

        # Calculate category tax
        tax_rate = tax_rates[category]
        tax = amount * tax_rate

        subtotal += amount
        total_tax += tax

        products.append({
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price,
            "amount": amount,
            "tax": tax
        })

    # Threshold-based discount
    if subtotal >= 10000:
        discount_rate = 0.15

    elif subtotal >= 5000:
        discount_rate = 0.10

    elif subtotal >= 1000:
        discount_rate = 0.05

    else:
        discount_rate = 0

    discount = subtotal * discount_rate

    # Maximum concession limit
    maximum_discount = 2000

    if discount > maximum_discount:
        discount = maximum_discount

    # Calculate final bill
    final_amount = subtotal - discount + total_tax

    # Generate invoice
    print("\n========== ITEMIZED INVOICE ==========")

    print(
        f"{'Product':15} {'Qty':5} "
        f"{'Price':10} {'Amount':10} {'Tax':10}"
    )

    print("-" * 60)

    for p in products:

        print(
            f"{p['name']:15} "
            f"{p['quantity']:<5} "
            f"{p['price']:<10.2f} "
            f"{p['amount']:<10.2f} "
            f"{p['tax']:<10.2f}"
        )

    print("-" * 60)

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount Rate:", discount_rate * 100, "%")
    print("Discount Amount: Rs.", round(discount, 2))
    print("Total Tax: Rs.", round(total_tax, 2))
    print("Final Payable Amount: Rs.",
          round(final_amount, 2))

    print("\nThank you for shopping!")
