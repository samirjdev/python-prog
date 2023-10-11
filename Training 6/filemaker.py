# Pseudocode:
# Start
# Open friends text file with write.
# Prompt for name, assign to name variable.
# While name does not equal nothing, prompt for age, assign to age value, convert to int.
# Write friend's name and age and add extra line.
# Close file.
# Prompt for name again, assign to name variable.
# While name equals nothing, print that the file was created.
# End

def main():

    f= open('friends.txt','w')

    name = input("Enter first name of friend or Enter to quit ")
    
    while name != '':
        
        age = int(input("Enter age (integer) of this friend "))
        f.write(name + '\n')
        f.write(str(age) + '\n')
        
        name = input("Enter first name of friend or Enter to quit ")

    f.close()
    print('File was created')
        
if __name__ == '__main__':
    main()

    
