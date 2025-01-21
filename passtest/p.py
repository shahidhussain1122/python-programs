import random
import string

# Base words
words = ["admin", "jawadusman", "jawad", "usman"]

# Special characters and numbers
special_chars = "!@#$%^&*"
numbers = "0123456789"

# Helper function to introduce variations
def generate_password_variations(word):
    variations = []
    # Add simple variations
    variations.append(word.lower())
    variations.append(word.upper())
    variations.append(word.capitalize())
    # Add special characters and numbers
    for char in special_chars:
        variations.append(word + char)
        variations.append(char + word)
    for num in numbers:
        variations.append(word + num)
        variations.append(num + word)
    return variations

# Generate a password list
passwords = set()
while len(passwords) < 1000:  # Limit to 1,000 passwords
    # Randomly pick 1 or 2 words
    selected_words = random.sample(words, random.randint(1, 2))
    base_password = ''.join(selected_words)
    
    # Apply variations
    variations = generate_password_variations(base_password)
    passwords.update(variations)
    
    # Randomly shuffle characters
    for _ in range(5):  # Add more randomness
        shuffled_password = ''.join(random.sample(base_password, len(base_password)))
        passwords.add(shuffled_password)
        # Add special chars or numbers to shuffled passwords
        passwords.add(shuffled_password + random.choice(special_chars) + random.choice(numbers))

# Save to file
with open("password_wordlist.txt", "w") as f:
    for password in list(passwords)[:1000]:  # Ensure the list is exactly 1,000
        f.write(password + "\n")

print("Generated 1,000 passwords in 'password_wordlist.txt'")
