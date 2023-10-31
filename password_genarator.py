import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/' if use_special_chars else ''
    
    # Combine character sets based on the user's choices
    characters = letters + digits + special_chars

    # Ensure the password length is at least 8 characters
    if length < 8:
        length = 8

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")
    password_length = int(input("Enter the desired password length: "))
    include_digits = input("Include digits (yes/no)? ").lower() in ['yes', 'y']
    include_special_chars = input("Include special characters (yes/no)? ").lower() in ['yes', 'y']

    generated_password = generate_password(password_length, include_digits, include_special_chars)
    print("Generated Password:", generated_password)
