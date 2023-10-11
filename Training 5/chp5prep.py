# Pseudocode:
# Start
# < For main function >
# Import random and math modules.
# Assign two random integers from 1 to 5 to variable 1 and variable 2 respectively.
# Call show_larger function.
# < For show_larger function >
# If number 1 is greater than number 2, find difference by subtracting number 1 from number 2 and print results.
# If number 2 is greater than number 1, find difference by subtracting number 2 from number 1 and print results.
# If number 1 equals number 2, print result showing they are equal.
# End

def main():

    import random
    import math
    
    var1 = random.randint(1,5)
    var2 = random.randint(1,5)
    
    show_larger(var1, var2)
    
def show_larger(num1, num2):

    if num1 > num2:
        diff = num1 - num2
        print(f'{num1} is larger by {num2} by {diff}')
    if num1 < num2:
        diff = num2 - num1
        print(f'{num2} is larger by {num1} by {diff}')
    if num1 == num2:
        print(f'The integers are equal, both are {num1}')

if __name__ == '__main__':
    main()

    
