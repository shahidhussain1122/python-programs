Courses = ("Web","AI","Cyber Security","App Dev","ML")
print(Courses)
print(type(Courses))
for course in Courses:
    print(course)

# change the tuple items 
# to change the tuple item first we have to change the tuple into list the we can change the list item and then again convert into tuple 
l = list(Courses)
print(type(l))

l[0] = "Web Dev"
t = tuple(l)
print(t)


# add item in tuple
fruits = ('Apple','Banana','Mango')
flist = list(fruits)
flist.append('Cherry')
fruits = tuple(flist)
print(fruits)

# add tuple to tuple

bs = ('BS')
cs  = ('CS')
bs+=cs
print(bs)

# Unpacking a Tuple

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

color = ("red", "blue", "orange")
(red,blue,orange) = color
print(red)
print(type(red))
print(blue)
print(type(blue))
print(orange)
print(type(orange))


# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


