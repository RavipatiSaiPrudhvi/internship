import random
import string

def generate_password(length=12):
    # Define character sets for different types of characters
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower_case + upper_case + numbers + symbols

    # Ensure at least one character from each set is included in the password
    password = random.choice(lower_case) + random.choice(upper_case) + random.choice(numbers) + random.choice(symbols)

    # Fill the rest of the password with random characters
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to make it more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password you want to generate: "))
    if length < 4:
        print("Password length should be at least 4.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
