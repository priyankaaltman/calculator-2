"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def main():
    while True:
        tokens = input("Enter a computation: ").split(" ")

        if tokens[0] == "q" or tokens[0] == "quit":
            print("Exiting...")
            break

        operation, num1 = tokens[0], float(tokens[1])

        float_list = []
        for item in tokens[1:]:
            float_list.append(float(item))

        if operation == "+":
            print(add(float_list))
        elif operation == "-":
            print(subtract(float_list))
        elif operation == "*":
            print(multiply(float_list))
        elif operation == "/":
            print(divide(float_list))
        elif operation == "square":
            print(square(float_list))
        elif operation == "cube":
            print(cube(float_list))
        elif operation == "pow":
            print(power(float_list))
        elif operation == "mod":
            print(mod(float_list))
        elif operation == "mult+":
            print(add_mult(float_list))
        elif operation == "cubes+":
            print(add_cubes(float_list))

if __name__ == '__main__':
    main()