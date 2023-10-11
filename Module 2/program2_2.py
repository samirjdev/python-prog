# Collaborators: none
# Pseudocode:
# Start
# Prompt for numerator, assign as numerator variable, convert as integer
# Prompt for denominator, assign as denominator variable, convert as integer
# Use arithmetic operator to do integer division (//) with the numerator by the denominator, assign as total variable
# Use arithmetic operator to find the remainder (%) of the numerator by the denominator, assign as remainder variable
# Print mixed number with total variable and remainder variable
# End

def main():
    numerator = int(input('Enter the numerator '))
    denominator = int(input('Enter the denominator '))
    total = numerator // denominator
    remainder = numerator % denominator
    print(f'As a mixed number that is {total} and {remainder}/{denominator}')
main()
