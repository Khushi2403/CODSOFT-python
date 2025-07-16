import random
import string

# Function to generate the password
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # All possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""  # Start with an empty password
    for i in range(length):
        random_char = random.choice(characters)  # Pick a random character
        password += random_char  # Add it to the password
    
    return password

# Main program
try:
    user_input = int(input("Enter the desired password length: "))
    password = generate_password(user_input)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
