# Pseudocode:
# Start
# Prompt for first test score, assign to first variable
# Prompt for second test score, assign to second variable
# Prompt for third test score, assign to third variable
# Add together the three variables and then divide them by 3, assign to total variable
# Print total variable stating completion

def main():
    
    first = float(input('Enter the score for test 1 '))
    second = float(input('Enter the score for test 2 '))
    third = float(input('Enter the score for test 3 '))
    total = (first + second + third) / 3 # Adds together the three scores and divides by 3 to make the average
    print(f'The average test score is {total:,.2f}%.')

main()
