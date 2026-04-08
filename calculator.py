import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a cannot be 0)")
    return b / a   # matches your definition

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Log argument must be positive")
    return math.log(b, a)  # log base a of b

def exponent(a, b):
    return a ** b





