"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm base and value must be positive numbers.")

    return math.log(a, b)

def exp(a, b):
    return a ** b



