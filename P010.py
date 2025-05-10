# Prime number
num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print(num,"is Not A Prime Number")
        break
else:
    print(num,"is A Prime Number")

# checking other conditions also like 1 is neither prime nor composite, 0 is zero, negative number is not prime

''' 
num=int(input("enter a number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is Not A Primer Number")
            break
    else:
        print(num,"is A Primer Number")
elif num==1:
    print(num,"is niether prime nor composite")
elif num==0:
    print(num,"is zero")
else:
    print(num,"is negative nuber")

'''