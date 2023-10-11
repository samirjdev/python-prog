# Pseudocode:
# Start
# Assign column variables to headers, print column with correct formatting using f-print.
# Use named constant to set tax rate of 7%.
# For subtotal in range of 20 to 520 in step of 20, use arithmetic operators.
# Divide subtotal by 100 to get new subtotal variable, and times the new subtotal variable by the tax rate to get the sales tax.
# Then, add the new subtotal variable with the sales tax to get the final total variable.
# Print the new subtotal, sales tax, and final total variables in the respective columns.
# End

def main():

    item1 = input('Enter item name ')
    unit1 = float(input(f'Enter unit price of {item1} '))
    quantity1 = float(input(f'Enter quantity of {item1} '))
    total1 = unit1 * quantity1
    quantity1int = int(quantity1)
    print(f'{quantity1int} {item1} @ ${unit1}, total ${total1:,.2f}')

    item2 = input('Enter item name ')
    unit2 = float(input(f'Enter unit price of {item2} '))
    quantity2 = float(input(f'Enter quantity of {item2} '))
    total2 = unit2 * quantity2
    quantity2int = int(quantity2)
    print(f'{quantity2int} {item2} @ ${unit2}, total ${total2:,.2f}')

    item3 = input('Enter item name ')
    unit3 = float(input(f'Enter unit price of {item3} '))
    quantity3 = float(input(f'Enter quantity of {item3} '))
    total3 = unit3 * quantity3
    quantity3int = int(quantity3)
    print(f'{quantity3int} {item3} @ ${unit3}, total ${total3:,.2f}')

    finaltotal = total1 + total2 + total3

    print(f'Total of these three items is ${finaltotal:,.2f}')
                    
     
main()
