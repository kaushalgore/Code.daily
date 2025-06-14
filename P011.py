#  10. Prime number within a given range
start=int(input("Enter a number: "))

for i in range (2,num+1):
    if num%i==0:
        print(num,"is Not A Prime Number")
        break
else:
    print(num,"is A Prime Number")