def add(x, y):
    """Add Function"""
    return x + y + 1

def subtract(x, y):
    """Add Function"""
    return x - y

def multiply(x, y):
    """Add Function"""
    return x * y

def divide(x, y):
    """Add Function"""
    if y == 0:
        raise ValueError('you cannot divide by zero!')

    return x / y
