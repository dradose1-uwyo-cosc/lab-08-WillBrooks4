# William Brooks
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section: 10
# Sources, people worked with, help given to:



# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def convert_to_num(num):
    isNeg = False
    if num[0] == "-":
        isNeg = True
        num=num.replace("-","")
    if "." in num:
        nums = num.split(".")
        if len(nums)==2 and nums[0].isdigit() and nums[1].isdigit():
            if isNeg:
                return (-1) * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isNeg:
            return (-1) * int(num)
        else:
            return int(num)
    else:
        return False




print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def equation(m, b, a, an):
    #function for equation
    y_list = []
    for x in range(a, an+1):
        y = m * x + b
        y_list.append(y)
    return y_list 

while True:
    m = False
    while m == False:
        slope = input("Please enter the slope")
        m = convert_to_num(slope)
        if slope.lower() == "exit":
            break
        if m == False:
            print(f"{slope} is not a valid number")
    
    if slope.lower() == "exit":
        break

    b = False
    while b == False:
        slope = input("Please enter the Y-intercept")
        b = convert_to_num(slope)
        if slope.lower() == "exit":
            break
        if b == False:
            print(f"{slope} is not a valid number")
    
    if slope.lower() == "exit":
        break

    a = False
    while a == False:
        slope = input("Please enter the Lower Bound")
        a = convert_to_num(slope)
        if slope.lower() == "exit":
            break
        if a == False:
            print(f"{slope} is not a valid number")
    
    if slope.lower() == "exit":
        break

    an = False
    while an == False:
        slope = input("Please enter the Upper Bound")
        an = convert_to_num(slope)
        if slope.lower() == "exit":
            break
        if an == False:
            print(f"{slope} is not a valid number")
    
    if slope.lower() == "exit":
        break

    y = equation(m, b, a, an)
    print(f"{y}")


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null