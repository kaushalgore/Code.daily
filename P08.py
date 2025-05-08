#   Greatest of the Three numbers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))  
c=int(input("Enter third number: "))
if a>b and a>c:
    print("Greatest number is: ",a)
elif b>a and b>c:
    print("Greatest number is: ",b)
elif c>a and c>b:
    print("Greatest number is: ",c)
else:
    print("All numbers are equal.")