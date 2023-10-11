# Pseudocode:
# Start
# For row in range of 10, and for column in range of 10 subtracted by row.
# Print column variable and end line, continue with next.
# Print pattern.
# End

def main():
    for r in range(10):
        for c in range(10-r):
            print(c, end="")
        print()
main()
