def multiplication_table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Call the function to execute
multiplication_table()