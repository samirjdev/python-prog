# Pseudocode:
# Start
# Prompt for integer or 0 to quit, assign to integer variable.
# Continue if integer does not equal 0.
# If integer has a remainer of 0, print that integer is an even number and prompt again for integer or 0 to quit.
# If else, print that integer is an odd number and prompt again for integer or 0 to quit.
# If integer equals 0, print finished result and end process.
# End

def main():
    
    integer = int(input('Enter an integer or 0 to quit '))
        
    while integer != 0:
        if (integer % 2) == 0:
            print(f'{integer} is an even number')
            integer = int(input('Enter an integer or 0 to quit '))
        else:
            print(f'{integer} is an odd number')
            integer = int(input('Enter an integer or 0 to quit '))

    print('All done!')
        

main()
