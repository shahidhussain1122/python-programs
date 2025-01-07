# write a python program to swap two number without using third variable
a = 5
b = 10
a = a + b  
b = a - b  
a = a - b  
print(a, b) 

# a = 5+10 = 15
# b = 15-10 = 5
# a = 15 - 5 = 10



# using third variable
a = 12
b = 24
c = a
a = b
b = c
print(a,b)

# using multiple assignment
a,b = 1,2
a,b = b,a
print(a,b)