#12. Reverse of a number
number = int(input("Enter a number: "))
reversed=0
while number > 0:
    digit = number % 10
    reversed=reversed.append(digit)
    number=number // 10
print("Reversed number is:", reversed)

