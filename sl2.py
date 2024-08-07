number = 1234
sum = 0

while number > 0:
       
       digit = number%10
       sum += digit
       number //= 10
    
print("Sum of digit:",sum)

