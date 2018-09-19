"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    tokens = input("Enter a computation: ").split(" ")

    operation = tokens[0]
    if operation == "q" or operation == "quit":
        print("Exiting...")
        break

    num1 = float(tokens[1])

    if len(tokens) == 3:
        num2 = float(tokens[2])

    if len(tokens) == 4:
        num3 = float(tokens[3])

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
        print(add_mult(num1, num2, num3))
    elif operation == "cubes+":
        print(add_cubes(num1, num2))

