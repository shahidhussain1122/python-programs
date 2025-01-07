# Python Lists
# List is a collection which is ordered and changeable. Allows duplicate members.
mylist = ["apple", "banana", "cherry"]
print(mylist)
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
# To determine how many items a list has, use the len() function:
print(len(thislist))

# List Items - Data Types
# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Python - Access List Items
# Access Items
# List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Negative Indexing
# Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

