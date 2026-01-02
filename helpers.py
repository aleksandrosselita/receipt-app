def handle_command(item,receipt,total,discount_rate,history,menu,):
    if item == "remove":
        history.append((receipt.copy(), total,discount_rate))
        receipt,total = remove_item_from_receipt (receipt,total)
        return receipt, total, discount_rate, True
    if item == "clear":
        history.append((receipt.copy(),total,discount_rate))
        receipt = []
        total = 0
        discount_rate = 0
        print (" receipt cleared")
        return receipt,total,discount_rate,True
    if item == "discount":
        history.append((receipt.copy(), total,discount_rate))
        discount_rate = get_discount_rate()
        print ("Discount applied.")
        return receipt, total, discount_rate, True
    
    if item == "undo":
        if history:
            receipt, total, discount_rate = history.pop()
            print("last actione undone")
        else:
            print("Nothing to undo ")
        return receipt,total,discount_rate, True
    return receipt, total, discount_rate, False

    

def get_discount_rate():
    while True:
        try:
            percent = int(input("Enter discount percentage (0-100): "))
            if 0 <= percent <= 100:
                return percent / 100
            else:
                print("Please enter a valid percentage between 0 and 100.")
        except ValueError:
            print("Please enter a number.")

def apply_discount(total, discount_rate):
    discount_amount = total * discount_rate
    final_total = total - discount_amount
    return discount_amount, final_total

def add_item_to_receipt(receipt, total, item, qty, price):
    cost = qty * price 
    receipt.append((item, qty, cost))
    total += cost
    return receipt, total
def test_calculate_cost():
    print("Testing calculate_cost...")

    result = calculate_cost(3, 5)
    if result == 15:
        print("  calculate_cost passed.")
    else:
        print(" calculate_cost failed.", result)

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
def remove_item_from_receipt(receipt, total):
    if len(receipt) == 0:
        print("Receipt is empty. Nothing to remove.")
        return receipt, total

    print("\nItems in receipt:")
    for i, (item, qty, cost) in enumerate(receipt, start=1):
        print(f"{i}) {item} x{qty} = ${cost:.2f}")

    while True:
        try:
            choice = int(input("Enter item number to remove (or 0 to cancel): "))
            if choice == 0:
                return receipt, total
            if 1 <= choice <= len(receipt):
                removed_item, removed_qty, removed_cost = receipt.pop(choice - 1)
                total -= removed_cost
                print(f"Removed: {removed_item} x{removed_qty} (-${removed_cost:.2f})")
                return receipt, total
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    test_calculate_cost()