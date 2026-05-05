# =========================
# PASSWORD GENERATOR
# =========================

# Import random module so we can choose random items
import random


# =========================
# ASCII TITLE
# =========================

print(r"""
__        __   _                          _ 
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)

        PASSWORD GENERATOR

""")


# =========================
# CHARACTER LISTS
# =========================

# List of lowercase letters
list_of_lower_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

# List of uppercase letters
list_of_upper_letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

# Combine uppercase and lowercase letters into one list
letters = list_of_upper_letters + list_of_lower_letters

# List of numbers as strings
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of symbols
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", "/", "?", "@"]


# =========================
# USER INPUT
# =========================

# Ask user how many letters they want
nr_letters = int(input("How many letters do you want in your password? "))

# Ask user how many numbers they want
nr_numbers = int(input("How many numbers do you want in your password? "))

# Ask user how many symbols they want
nr_symbols = int(input("How many symbols do you want in your password? "))


# =========================
# CREATE EMPTY PASSWORD LIST
# =========================

# This list will store all random characters
password_list = []


# =========================
# ADD RANDOM LETTERS
# =========================

# Repeat as many times as the user asked for letters
for letter in range(nr_letters):

    # Choose one random letter
    random_letter = random.choice(letters)

    # Add random letter to password list
    password_list.append(random_letter)


# =========================
# ADD RANDOM NUMBERS
# =========================

# Repeat as many times as the user asked for numbers
for number in range(nr_numbers):

    # Choose one random number
    random_number = random.choice(numbers)

    # Add random number to password list
    password_list.append(random_number)


# =========================
# ADD RANDOM SYMBOLS
# =========================

# Repeat as many times as the user asked for symbols
for symbol in range(nr_symbols):

    # Choose one random symbol
    random_symbol = random.choice(symbols)

    # Add random symbol to password list
    password_list.append(random_symbol)


# =========================
# SHUFFLE PASSWORD
# =========================

# Shuffle the list so the password order is random
random.shuffle(password_list)


# =========================
# CREATE FINAL PASSWORD
# =========================

# Join all characters from the list into one string
password = "".join(password_list)


# =========================
# FINAL OUTPUT
# =========================

# Print the generated password
print(f"\nYour generated password is: {password}")