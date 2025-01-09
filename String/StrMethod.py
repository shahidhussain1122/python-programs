s = "hello"
print(len(s)) # to fine length of string
print(s.upper()) # to convert string to upper case
print(s.lower())    # to convert string to lower case
print(s.capitalize())  # to convert first letter of string to upper case
print(s.title())  # to convert first letter of each word to upper case
print(s.swapcase()) # to convert upper case to lower case and vice versa
print(s.center(20)) # to center the string
print(s.ljust(20)) # to left justify the string
print(s.rjust(20)) # to right justify the string
print(s.zfill(20)) # to fill the string with zeros
print(s.count('l'))    # to count the number of times a substring occurs in a string
print(s.find('l')) # to find the first occurrence of a substring in a string
print(s.rfind('l'))   # to find the last occurrence of a substring in a string
print(s.index('l'))  # to find the first occurrence of a substring in a string
print(s.rindex('l')) # to find the last occurrence of a substring in a string
print(s.replace('l', 'L'))  # to replace a substring with another substring
print(s.split('l')) # to split a string into a list of substrings
print(s.rsplit('l'))   # to split a string into a list of substrings
print(s.splitlines()) # to split a string into a list of lines
print(s.startswith('h'))   # to check if a string starts with a substring
print(s.endswith('o')) # to check if a string ends with a substring
print(s.isalnum()) # to check if a string is alphanumeric
print(s.isalpha()) # to check if a string is alphabetic
print(s.isdigit()) # to check if a string is numeric
print(s.islower())  # to check if a string is in lower case
print(s.isupper()) # to check if a string is in upper case
print(s.isspace())  # to check if a string contains only whitespace
print(s.istitle()) # to check if a string is in title case
print(s.join('123'))   # to join a list of strings with a string
print(s.strip())   # to remove leading and trailing whitespace
print(s.lstrip()) # to remove leading whitespace
print(s.rstrip()) # to remove trailing whitespace


str = "hello world"
if str.startswith("hello"):
    print("String starts with 'hello'")
    
if str.endswith("world"):
    print("String ends with 'world'")
    
if str.islower():
    print(str.upper())
    
if str.isupper():
    print(str.lower())