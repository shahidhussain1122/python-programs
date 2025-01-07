a, b = 0, 1
for i in range(20):
    if i == 0:
        print(a)
    elif i == 1:
        print(b)
    else:
        next_number = a + b
        print(next_number)
        a, b = b, next_number
