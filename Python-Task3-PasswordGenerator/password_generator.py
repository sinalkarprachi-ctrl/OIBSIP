import random
import string

print("Random Password Generator")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase")
        print("2. Lowercase")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter at least 2 choices (example: 123): ")

        if len(set(choices)) < 2:
            print("Please choose at least 2 different character types.")
            continue

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

        again = input("Do you want to generate another password? (yes/no): ")

        if again.lower() != "yes":
            break

    except ValueError:
        print("Please enter a number for password length.")