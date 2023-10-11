# Pseudocode:
# Start
# < For main >
# Prompt for radius, assign to radius variable, convert to float.
# Call area of circle function, print returned result from function.
# Call circumference of circle function.
# End
# < For area_of_circle >
# Import math module.
# Calculate area with pi times the radius squared.
# Return circle area.
# End
# < For circumference_of_circle >
# Import math module.
# Calculate circumference with pi * 2 * radius.
# Print result of circumference.
# End

def main():
    
    radius = float(input('Enter radius of circle '))
    circle_area = area_of_circle(radius)
    print(f'The area of a circle with radius {radius} is {circle_area:,.4f}')
    circumference = cir_of_circle(radius)

def area_of_circle(rad):
    import math
    circle_area = math.pi * rad**2
    return circle_area

def cir_of_circle(rad):
    import math
    circle_cir = 2 * math.pi * rad
    print(f'The circumference is {circle_cir:,.3f}')
    
if __name__ == '__main__':
    main()
