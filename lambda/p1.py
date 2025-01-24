'''What is a Lambda Function?
A lambda function in Python is a small anonymous function. It allows you to create a function inline without declaring it separately 12.

Key points about lambda functions:

They are defined using the lambda keyword
They consist of a single expression
They can take any number of arguments
They are typically used for short, simple functions'''

greet = lambda name:f"hello {name}"
print(greet("Ninja"))


# another example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 


squared_numbers = list(map(lambda x:x**2, numbers))
print(squared_numbers)
