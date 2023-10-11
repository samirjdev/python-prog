# Collaborators: none
# Pseudocode:
# Start
# Prompt for miles, assign to miles variable, convert as floating point number
# Use arithmetic operators to multiply miles by KILOMETERS_CONVERSION (named constant) to convert to kilometers, assign to kilometers variable
# Print the miles with the kilometers being rounded to three decimal places
# End

def main():
    miles = float(input('Enter the miles '))
    KILOMETERS_CONVERSION = 1.60934 # The number represents the miles to kilometers conversion factor
    kilometers = miles * KILOMETERS_CONVERSION
    print(f'{miles} miles is {kilometers:,.3f} kilometers')
main()

