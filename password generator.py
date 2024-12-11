import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    # Start with lowercase letters
    characters = string.ascii_lowercase
    
    # Add additional character types based on user preference
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User inputs
print("Welcome to the Password Generator!")
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

# Generate and display the password
password = generate_password(length, include_uppercase, include_numbers, include_special)
print(f"Your generated password is: {password}")
