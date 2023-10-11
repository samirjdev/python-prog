# Pseudocode:
# Start
# < For celsius to fahrenheit function >
# Use arithmetic operators to convert celsius to fahrenheit, assign to fahrenheit variable, convert to float.
# Print result with celsius value and fahrenheit value.
# < For fahrenheit to celsius function >
# Use arithmetic operators to convert fahrenheit to celsius, assign to celsius variable, convert to float.
# Return celsius variable.
def c_to_f(celsius):
    fahrenheit = float(celsius * 1.8 + 32)
    print(f'{celsius} Celsius is {fahrenheit:.1f} Fahrenheit')


def f_to_c(fahrenheit):
    celsius = float((fahrenheit - 32) * (5/9))
    return celsius
