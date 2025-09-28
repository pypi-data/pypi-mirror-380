def add(a, b):
    """Return sum of two numbers"""
    return a + b

def multiply(a, b):
    """Return product of two numbers"""
    return a * b

def divide(a, b):
    """Return division of a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
