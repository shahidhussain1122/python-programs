import re

#original string
string1 = "Hello!Khan,Pakistan"

pattern = r'[0-9]'

new_string = re.sub(pattern, '', string1)

print(new_string)