# Sum of N natural numbers
# 1. Write a Python program to find the sum of N natural numbers using recursion.
# 2. Write a Python program to find the sum of N natural numbers using iteration.
# 3. Write a Python program to find the sum of N natural numbers using lambda function.
# 4. Write a Python program to find the sum of N natural numbers using list comprehension.  
# 5. Write a Python program to find the sum of N natural numbers using map function.
# 6. Write a Python program to find the sum of N natural numbers using filter function.
# 7. Write a Python program to find the sum of N natural numbers using reduce function.
# 8. Write a Python program to find the sum of N natural numbers using functools module.
# 9. Write a Python program to find the sum of N natural numbers using operator module.
# 10. Write a Python program to find the sum of N natural numbers using math module.
# 11. Write a Python program to find the sum of N natural numbers using numpy module.
# 12. Write a Python program to find the sum of N natural numbers using pandas module.

num=int(input("enter number to find sum upto n:"))
# def recursive_sum(n):
#     # Base case: if n is 1, return 1
#     if n == 1:
#         return 1
#     # Recursive step: n plus sum of (n-1)
#     return n + recursive_sum(n - 1)

# print(recursive_sum(num))  # Outputs 55

def recusrion_sum(num):
    if num==1:
        return 1
    return 1+recusrion_sum(num-1)
print(recusrion_sum())


















