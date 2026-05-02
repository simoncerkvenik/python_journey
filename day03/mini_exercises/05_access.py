# Mini Exercise - Nested If
# Goal: Practice an if statement inside another if statement

# Correct password for the vault
pass_access = "simon1"

# Welcome message
print("Welcome to the vault")

# Ask the user to enter a password
password = input("Please enter your password: ")

# Check if the password is correct
if password == pass_access:

    # If the password is correct, ask the user for their age
    age = int(input("Please enter your age: "))

    # Check if the user is 18 or older
    if age >= 18:
        print("Access granted.")
    else:
        print("You are too young.")

# If the password is wrong
else:
    print("Wrong password.")