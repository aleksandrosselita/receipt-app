



def calculate_cost(qty, price ):
    return qty * price
def print_receipt( receipt, total ):
    print("\n----- Receipt -----")
    for item, qty, cost in receipt:
        print(f"{item} (x{qty}): ${cost:.2f}")
    print(f"Total: ${total:.2f}")

def get_item(menu):
    while True:
        item = input ("Enter item (beer, wine, cocktail) or 'done' : ")
        
        if item == "done" :
            return "done"
        
        if item in menu:
            return item
        print ("item not on menu . ")
        
def get_quantity(item):
    while True:
        try:
            qty = int(input(f"how many {item} would you like ? "))
            if qty >0:
                return qty
            print (" quantity must be greater than zero . ")
        except ValueError:
            print ( "please enter a number.")

menu = {
    "beer": 5,
    "wine": 8,
    "cocktail": 12
}

total = 0
receipt = []

while True:
    item = get_item(menu)

    if item == "done":
        break

    qty = get_quantity(item)

    cost = calculate_cost(qty, menu[item])
    total += cost
    receipt.append((item, qty, cost))
    
print_receipt(receipt, total)


