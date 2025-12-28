print("Welcome to the Receipt App")

menu = {
    "beer": 5,
    "wine": 8,
    "cocktail": 12
}

total = 0
receipt = []

# 1) Collect items
while True:
    item = input("Enter item name (or 'done'): ").strip().lower()

    if item == "done":
        break

    if item not in menu:
        print("Item not on menu.")
        continue

    while True:
        try:
            qty = int(input(f"How many {item}? "))
            if qty < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a number.")

    cost = qty * menu[item]
    total += cost
    receipt.append((item, qty, cost))

# 2) Print receipt
print("\n--- RECEIPT ---")
for item, qty, cost in receipt:
    print(f"{item} x{qty} = ${cost:.2f}")

print(f"Subtotal: ${total:.2f}")

# 3) Ask discount ONCE (after done)
tax_rate = 0.08

while True:
    try:
        discount_percent = int(input("Enter discount % (0, 10, 20): "))
        if discount_percent in [0, 10, 20]:
            discount_rate = discount_percent / 100  # 10 -> 0.10
            break
        else:
            print("Only 0, 10, or 20 allowed.")
    except ValueError:
        print("Enter a number.")

# 4) Totals
tax = total * tax_rate
discount = total * discount_rate
final_total = total + tax - discount

print("\n--- TOTAL ---")
print(f"Tax: ${tax:.2f}")
print(f"Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
