#  PrepInsta Top 100 Codes 
#  Write a program to check whether a number is even or odd.

num=int(input("Enter a number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

'''
#Good Practice to add exception handling for invalid input (like strings).
#handling for invalid input (like strings). 
#code starts here
try:
    num=int(input("Enter a number:"))
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")
except ValueError:
    print("Invalid input, please enter a number.")
'''