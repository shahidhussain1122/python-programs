# Python - Modify Strings
# Upper Case

a = "Hello, World!"
print(a.upper())


# Lower Case

# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


string1 = "helo, ali, how, are, you ?"
print(string1.split(","))