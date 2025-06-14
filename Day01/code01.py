#  11. Sum of digits of a number

number=int(input("Enter A number: "))
sum=0
while number>0:
    digit=number%10
    sum+=digit
    number=number//10
print("Sum of digits is:",sum)

''' **************************Handle Negative number and more********************************** '''


number=int(input("Enter A number: "))
total=0  #sum is a built-in function, so using total instead
original_number = number  # Store the original number for later use
original_number = abs(original_number)  # Handle negative numbers by taking absolute value

while number>0:
    digit=original_number%10
    total+=digit    
    number=number//10
print("Sum of digits is:",total)


