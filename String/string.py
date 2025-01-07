# Python Strings
'''
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
'''

print("Hello")
print('Hello')


# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("hello it's")
print('helo it"s"')



# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

str = "this iis string"

print(str)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)




# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)
  
for i in "helo":
  print(i)
  
#   String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

text = "that the quick brown fox jumps over the lazy dog"
print("Length : ",len(text))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

email = "ali@gmail.com"
print('4' in email)
if '@' in email:
  print("login successfull")
else:
  print("Not found")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)




# Python - Slicing Strings
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string

b = "Hello, World!"
print(b[2:5])

txt = "Hi my name is ali"
print(txt[14:18])
print(txt[:18])
print(txt[2:])


# Slice From the Start
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:

b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-6:-1])


