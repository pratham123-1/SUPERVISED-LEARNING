#prime no
n= int(input("enter the no,"))

flag = True
print("the entered values is :",n)

for i in range(2,n):
    if(n%i==0):
        flag=False
        break
if(flag):
        print("prime number")

else:
     print("not a prime number")
        