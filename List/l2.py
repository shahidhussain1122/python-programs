# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Python - Change List Items
# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Python - Add List Items
# Append Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear the ListThe clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)