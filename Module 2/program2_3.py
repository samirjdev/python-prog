# Collaborators: none
# Pseudocode:
# Start
# Prompt for unit price of item, assign to price variable, convert to floating point number
# Prompt for unit quantity, assign to quantity variable, convert to integer
# Use arithmetic operators to multiply price by qty, assign to subtotal variable
# Use arithmetic operators to multiply subtotal by SALES_TAX (named constant) for sales tax, assign due tax variable
# Use arithmetic operators to add subtotal and due tax to create final total, assign to total variable
# Print subtotal variable rounded to 2 decimal points with commas
# Print due tax variable rounded to 2 decimal points with commas
# Print total variable rounded to 2 decimal points with commas
# End

def main():
    price = float(input('Enter the item\'s unit price '))
    qty = int(input('Enter the quantity '))
    subtotal = price * qty
    SALES_TAX = 0.07
    duetax = subtotal * SALES_TAX
    total = subtotal + duetax
    print(f'The subtotal is ${subtotal:,.2f}')
    print(f'Sales tax is ${duetax:,.2f}')
    print(f'Total due is ${total:,.2f}')
main()
    
    
                        
