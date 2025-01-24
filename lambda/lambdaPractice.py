greet = lambda name: f"Hello {name}"
print(greet("Ali"))

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x : x % 2==1, numbers))
print(odd_numbers)

def evenNumber(x):
    for i in x:
        if i % 2 == 0:
            print(i)
        else:
            pass
numbers = [12,3,4,5,6]
evenNumber(numbers)


