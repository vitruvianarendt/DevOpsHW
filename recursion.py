def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


input_number = 3
print("The factorial of", input_number, "is: ", factorial(input_number))