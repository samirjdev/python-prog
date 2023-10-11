# Pseudocode:
# Start
# Calculate subtotal using number and value variables, assign to subtotal variable.
# Print subtotal and round to 2 decimal places.
# End

def total(name, val, num):
    calctotal = num * val
    print(f'Item: {name}, subtotal: ${calctotal:.2f}')
    
    
