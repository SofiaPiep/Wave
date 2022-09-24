def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero")


