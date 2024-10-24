def print_pyramid():
    # Ask the user for the number of levels
    levels = int(input("Enter the number of levels for the pyramid: "))
    
    # Print the pyramid
    for i in range(1, levels + 1):
        # Print spaces on the left for centering the pyramid
        print(' ' * (levels - i), end='')
        # Print the pyramid layer (2*i - 1 stars)
        print('*' * (2 * i - 1))

# Call the function
print_pyramid()
