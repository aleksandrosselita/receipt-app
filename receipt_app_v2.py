



def calculate_cost(qty, price ):
    return qty * price
def print_receipt( receipt, total ):
    print("\n----- Receipt -----")
    for item, qty, cost in receipt:
        print(f"{item} (x{qty}): ${cost:.2f}")
    print(f"Total: ${total:.2f}")

menu = {
    "beer": 5,
    "wine": 8,
    "cocktail": 12
}

total = 0
receipt = []

while True:
    item = input("Enter item (beer, wine, cocktail) or 'done' to finish: ")

    if item == 'done':
        break

    if item not in menu:
        print("Item not on menu. Please try again.")
        continue

    while True:
        try:
            qty = int(input(f"Enter quantity of {item}: "))
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    cost = calculate_cost(qty, menu[item])
    total += cost
    receipt.append((item, qty, cost))

print_receipt(receipt, total)
