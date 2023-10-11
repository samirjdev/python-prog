# Pseudocode:
# Start
# Prompt user for item name, assign to item variable
# Prompt user for price, assign to price variable, convert to float
# Prompt user for quantity, assign to qty variable
# Calculate subtotal multiplying price by qty and storing into sub variable
# Print bill: qty item @ price cost, which will be sub and include 2 decimals
# End
def main():
    item_name = input('Enter item name ') # prompt user for item name, stores value
    price = float(input('Enter unit price '))
    qty = int(input('Enter quantity '))
    sub = price * qty
    print(f'{qty} {item_name} @ {price} cost ${sub:,.2f}')
main()
