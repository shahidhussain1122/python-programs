# password_generator.py
import random
import string

# control the number of each type of character
def password_generator(size, upper=1, lower=1, digits=1, symbols=1):
    chars = ''
    password = ''
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    # make sure the password has at least one of each type of character
    if upper:
        password += random.choice(string.ascii_uppercase)
    if lower:
        password += random.choice(string.ascii_lowercase)
    if digits:
        password += random.choice(string.digits)
    if symbols:
        password += random.choice(string.punctuation)

    # add the rest of the characters
    for i in range(size - 4):
        password += random.choice(chars)

    # shuffle the characters
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    return password

print(password_generator(16, True, True, True, True))
print(password_generator(8, False, True, False, True))