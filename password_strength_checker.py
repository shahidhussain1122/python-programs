# Password Strength Checker in Python
def password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
        
    if strength == 1:
        return 'Weak'
    elif strength == 2:
        return 'Medium'
    elif strength == 3:
        return 'Strong'
    elif strength == 4:
        return 'Very Strong'
    elif strength == 5:
        return 'Extremely Strong'
        
# get the password from the user
password = input('Enter your password: ')
print('Password Strength:', password_strength(password))