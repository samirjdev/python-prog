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

    column1 = 'SUBTOTAL'
    column2 = 'SALES TAX'
    column3 = 'TOTAL'
    column4 = '--------'
    column5 = '---------'
    column6 = '-----'

    TAX_RATE = 0.0007

    print(f'{column1:^9}{column2:^9}{column3:^9}')
    print(f'{column4:^9}{column5:^9}{column6:^9}')
    for subtotal in range(20,520,20):

        subtotal2 = subtotal / 100
        salestax = subtotal * TAX_RATE
        finaltotal = subtotal2 + salestax

        print(f'{subtotal2:^9,.2f}{salestax:^9,.2f}{finaltotal:^9,.2f}')
     
main()

