# Pseudocode:
# Start
# Open friends text file with read.
# Assign total value and count value to 0.
# While name does not equal nothing, read name and age and print both, add age to total and add one to count.
# Close file, average equals total divided by count, print average.
# End

def main():

    f = open('friends.txt','r')
    
    total = 0
    count = 0

    name = f.readline()

    while name != '':
        name = name.rstrip('\n')
        age = int(f.readline())
        print(f'My friend {name} is {age}')
        total += age
        count += 1

        name = f.readline()

    f.close()
    average = total / count
    print(f'Average age of friends is {average:.1f}')
        
if __name__ == '__main__':
    main()

