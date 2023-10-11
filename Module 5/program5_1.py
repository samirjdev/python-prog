# Pseudocode:
# Start
# Prompt for number of items, assign to number variable.
# Correct range of items by adding + 1 to number variable.
# Set current total value to 0
# For item in range of 1 to amount of items listed, prompt for description, price, and quantity.
# Import totalcalc module to calculate subtotal and print it, then repeat process.
# By end, add the calculated subtotals together to the total value variable.
# Print the total value variable.
# End

def main():


    number = int(input('How many different items are being purchased? '))
    correction = number + 1
    totalvalue = 0
    for item in range(1, correction):
        description = input(f'Enter description of item {item} ')
        price = float(input(f'Enter price of item {item} '))
        quantity = int(input(f'Enter the quantity for item {item} '))
        from totalcalc import total
        total(description, price, quantity)
        
        totalvalue = totalvalue + (price * quantity)

    print('     ')
    print(f'Your total is ${totalvalue:.2f}')

        
if __name__ == '__main__':
    main()

    
