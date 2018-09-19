"""Math functions for calculator."""


def add(input):
    """Return the sum of the two inputs."""

    return input[0] + input[1]

def subtract(input):
    """Return the second number subtracted from the first."""

    return input[0] - input[1]

def multiply(input):
    """Multiply the two inputs together."""

    return input[0] * input[1]

def divide(input):
    """Divide the first input by the second and return the result."""

    return input[0] / input[1]

def square(input):
    """Return the square of the input."""

    return input[0]**2

def cube(input):
    """Return the cube of the input."""

    return input[0]**3

def power(input):
    """Raise input[0] to the power of input[1] and return the value."""

    return input[0]**input[1]

def mod(input):
    """Return the remainder of input[0] / input[1]."""

    return input[0] % input[1]

def add_mult(input):
    """Return the sum of the first two numbers multiplied by the third number."""

    return (input[0] + input[1]) * input[2]

def add_cubes(input):
    """Return the sum of two cubes."""

    return input[0]**3 + input[1]**3
    