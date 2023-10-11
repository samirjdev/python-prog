# Pseudocode:
# Start
# Assign column headers to variables column 1, 2, and 3.
# Print headers using appropriate spacing and placement.
# For integers in range from 5 to 55, step 5.
# Use the exponent operator and assign squares as integers by 2 and cubes as integers by 3.
# Prints integers, squares, and cubes in appropriate columns with commas displayed.
# End

def main():

    column1 = 'INTS'
    column2 = 'SQUARES'
    column3 = 'CUBES'

    print(f'{column1:^7}{column2:>8}{column3:>12}')
    for ints in range(5, 55, 5):
        squares = ints ** 2
        cubes = ints ** 3

        print(f'{ints:^7,}{squares:>8,}{cubes:>12,}')
     

main()
