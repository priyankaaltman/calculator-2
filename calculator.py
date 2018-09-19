"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

# Your code goes here

exit = False
while exit == False:
    selection =input("Enter a computation: ")
    tokens = selection.split(" ")

    operation = tokens[0]
    num1 = float(tokens[1])
    num2 = float(tokens[2])

    if operation == "+":
        print(add(num1, num2))
    elif operation == "-":
        print(subtract(num1, num2))
    elif operation == "*":
        print(multiply(num1, num2))
    elif operation == "/":
        print(divide(num1, num2))
    elif operation == "square":
        print(square(num1))
    elif operation == "cube":
        print(cube(num1))
    elif operation == "pow":
        print(power(num1, num2))
    elif operation == "mod":
        print(mod(num1, num2))
    elif operation == "mult+":
        num3 = float(tokens[3])
        print(add_mult(num1, num2, num3))
    elif operation == "cubes+":
        print(add_cubes(num1, num2))
    elif operation == "q" or operation == "quit":
        exit = True
        print("Exiting...")



