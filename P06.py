#Sum of numbers in a given range

start_point=int(input("Enter the start point: "))
end_point=int(input("Enter the end point: "))
addition=0 #avoid using sum as it is a built-in function
for i in range(start_point,end_point+1):
    addition=addition+i
print("The sum of numbers in the given range is: ",addition)


''' 
1) Check strat point is less than end point or equal to end point.
# If not, print an error message and exit the program.
2) Good Practice to add exception handling for invalid input (like strings).

#code starts here

try:
    start_point=int(input("Enter the start point: "))
    end_point=int(input("Enter the end point: "))

    if start_point>end_point:
        print("Error: Start point should be less than or equal to end point.")
        exit(1)
    else:
        print(sum(start_point,end_point+1))
except ValueError:
    print("Invalid input, please enter a number.")
''' 
