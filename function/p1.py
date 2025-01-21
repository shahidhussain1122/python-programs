'''Definition and Purpose
A Python function is a block of code that performs a specific task. It is defined using the def keyword and can take input parameters and return output values 1.

Key points:

Functions encapsulate reusable code
They increase code readability and reusability
Functions can take parameters (arguments) and return values
Syntax and Structure
The basic syntax for defining a Python function is:'''

'''def function_name(parameters):
    # Function body
    pass'''

# example
def greet():
    print("Hello, World!")
greet()
# example 1

def add():
    a,b = 10,30
    sum = a+b
    print(sum)
add()

# example2

def addition(a,b):
    sum = a+b
    return sum
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
result = addition(no1,no2)
print(result)