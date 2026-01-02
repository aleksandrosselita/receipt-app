
from helpers import  get_discount_rate, handle_command, print_receipt, get_item, get_quantity, add_item_to_receipt, remove_item_from_receipt, apply_discount



menu = {
    "beer": 5,
    "wine": 8,
    "cocktail": 12
}

total = 0
receipt = []
discount_rate = 0
discount_amount = 0
history = []

while True:
    item = input ("Enter item , 'remove', 'discount','undo','clear' or 'done' : ")
    if item == "done":
        break
    receipt, total, discount_rate, handled = handle_command( 
    item, receipt, total, discount_rate, history, menu

)
    if handled:
        continue
    
    if item not in menu:
        print("Item not in menu")
        continue    

    qty = get_quantity(item)
    history.append((receipt.copy(), total, discount_rate))
    receipt, total = add_item_to_receipt(receipt, total, item, qty, menu[item])
    
discount_amount, final_total = apply_discount ( total, discount_rate)
print_receipt (receipt, final_total)
print (f"Discount: - ${discount_amount:.2f}")