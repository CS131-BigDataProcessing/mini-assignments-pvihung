import math_functions
def power(a, b): 
    return a ** b

def divide(a, b):
    if b == 0: 
        # Raise-Bao ra exception 
        raise ValueError("Can not divide a number by zero")
    return a/b
