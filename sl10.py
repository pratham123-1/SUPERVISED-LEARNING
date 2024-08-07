def print_number_pattern():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(str(i) * i)
print_number_pattern()