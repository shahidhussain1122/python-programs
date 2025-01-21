# Python Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) 
#before the change

car["color"] = "white"
print(x) 

# Get Values
# The values() method will return a list of all the values in the dictionary.

x = thisdict.values()

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

x = thisdict.items()


