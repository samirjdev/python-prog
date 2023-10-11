# Pseudocode:
# Start
# Prompt for temperature, assign to temp variable, convert to int.
# Prompt for fahrenheit or celsius, assign to temp scale variable.
# If temp scale is celsius, import celsius to fahrenheit conversion from temps module.
# Call function.
# End
# If temp scale is fahrenheit, import fahrenheit to celsius conversion from temps module.
# Call function, assign to cconvert.
# Using returned values, print result with temp value and cconvert value.
# End

def main():
    
    temp = int(input('Enter a temperature '))
    tempscale = input('Was that input Fahrenheit or Celsius c/f? ')

    if tempscale == 'c':
        from temps import c_to_f
        c_to_f(temp)
    
    if tempscale == 'f':
        from temps import f_to_c
        cconvert = f_to_c(temp)
        # return values
        print(f'{temp} Fahrenheit is {cconvert:.1f} Celsius')

if __name__ == '__main__':
    main()
