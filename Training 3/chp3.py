# Collaborators: none
# Pseudocode:
# Start
# Print for how many pounds ordered, assign to pounds variable, convert to int
# Use boolean expressions to assign pounds variable with correct pricing
# Multiply price by pounds variable to receive cost of coffee, assign to cost variable
# Multiply 7% sales tax by cost variable to receive cost of tax, assign to due tax variable
# Add due tax variable with cost variable, assign to total variable
# If cost variable is over 150, add tax to total variable, assign  
# End

def main():
    pounds = int(input('How many pounds are you ordering? '))

    if pounds >= 40:
        cost = pounds * 7.50
    if pounds < 40 and pounds >= 20:
        cost = pounds * 8.75
    if pounds < 20 and pounds >= 10:
        cost = pounds * 10
    if pounds < 10 and pounds >= 1:
        cost = pounds * 12
    print(f'Cost of coffee ${cost:,.2f}')
    
    duetax= 0.07 * cost
    print(f'7% sales tax ${duetax:,.2f}')
    
    if cost <= 150:
        cost = cost + 15
        print('Shipping fee $15.00')

    elif:
        print('Shipping fee $0.00')
        
    totalcost = cost + duetax
    print(f'Total payable ${totalcost:,.2f}')
main()
