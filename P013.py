#pallindrome
num=input("Enter a number: ")
reversed_num=num[::-1]
if num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


# Compare this snippet from P013.py:
# 13. Reverse of a number   
number = int(input("Enter a number: "))
reversed_num = 0    
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10
print("Reversed number is:", reversed_num)
if str(reversed_num) == str(number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")