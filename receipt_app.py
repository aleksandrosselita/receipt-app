print ("welcome to the receipt app")

menu = {
    "beer": 5,
    "wine": 8,
    "cocktails":12, 
}

total = 0 

for item, price in menu.items():
    while True:
        try:
            qty = int(input(f"How many {item}? "))
            break
        except ValueError:
            print("Please enter a number.")
    
    total = total + (qty * price)

print("Subtotal:", total)
tax = total * 0.08
discount = total * 0.20

final = total + tax - discount

print(f"Final total: ${final:.2f}")