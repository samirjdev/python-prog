# Start
# < For main function >
# Import random module.
# Create empty list named numbers.
# Create a for loop for n in range of 12.
# Create a random integer between 50 to 100.
# Print 4th element in the list, index 9 elment, and smallest element.
# Call change_list function with numbers as the argument.
# Using returned list, assign to list2, and use a for loop to display the elements together.
# End
# < For show_larger function >
# Get rid of the six middle elements, assign to numbers2.
# Print size of the numbers2 list and sort in ascending order, then return the list.
# End

import random

def main():

    integers = []
    cel_int = [random.randint(-40,40) for i in range(50)]     
    print(f'Lowest temp is',min(cel_int), 'C and highest is',max(cel_int), 'C')

    if 0 not in cel_int:
        print('No zero value found')

    if 0 in cel_int:
        zero = cel_int.index(0)
        print('Found 0C at index', (zero))

    print('Sorted sample of ten equivalent temperatures')

    COL1 = CELSIUS
    COL2 = FAHRENHEIT

    print(f'{COL1:^9}{COL2:^9}')

    cel_int_sub = random.cel_int(1,10)


    

    for num in numbers:
        print(num,end=' ')
    print('\nThe 4th element in the list is', numbers[3])
    print('The element at index 9 is', numbers[9])
    print('The smallest element in the list is', min(numbers))

    list2 = change_list(numbers)
    print('change_list returned this sorted list...')
    for num in list2:
        print(num, end=' ')

def change_list(secondlist):

    numbers2 = secondlist[3:-3]
    print('The size of the list is now', len(numbers2))
    numbers2.sort()
    return numbers2

if __name__ == '__main__':
    main()

    
