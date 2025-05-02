#  PrepInsta Top 100 Codes 
#  Sum of First N Natural numbers

num=int(input("Enter a number : "))
addition=0
for i in range(1,num+1):
    addition=addition+i #or-> sum+=i
print("Sum of first",num,"natural numbers is",addition)


################### Another way to do it ###################
''' 
# using direct formula to calculate sum of first n natural numbers.
# Formula: n*(n+1)/2

#code starts here 
num=int(input("Enter a number : "))
sum=num*(num+1)/2
print(sum)      #or-> print(int(sum))

'''  
################### Another way to do it ###################
''' 
# using sum function from python library. 
# sum(iterable, start) : 
    iterable: (list, tuple, etc.) of numbers you want to sum.
    start (optional): The default value of start is 0.
# sum  is a built-in function in Python that takes an iterable (like a list or tuple) and returns the sum of its elements.
# Docs link : https://docs.python.org/3/library/functions.html#sum

# code starts here
num=int(input("Enter a number : "))
addition = sum(range(1,num+1)) #or-> sum(range(1,num+1),0)
print("Sum of first",num,"natural numbers is",addition)

'''

################### final version ###################
''' 
# using exception handling for invalid input (like strings).
# handle numbers other than natureal numbers (like negative numbers).

# code starts here
try :
    num= int(input("Enter a number : "))
    if (num<1):
        print("Please enter greater than 0")
    else:
        addition = sum(range(1,num+1))
        print("Sum of first",num,"natural numbers is",addition)
except ValueError:
    print("Invalid input, please enter a number.")
'''

