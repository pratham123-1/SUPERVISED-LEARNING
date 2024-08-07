def print_star_pattern():
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows + 1):
        print('*' * i)

# Call the function to execute
print_star_pattern()