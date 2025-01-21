# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)


# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Get the Length of a Set

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
