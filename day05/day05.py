# PASSWORD GENERATOR - LOGIC ONLY

# 1. Import the module that lets you choose random items

# 2. Create a list of letters
# include lowercase and uppercase letters

# 3. Create a list of numbers
# keep them as strings, not integers
# example: "0", "1", "2"

# 4. Create a list of symbols
# example: "!", "#", "$", "%", "&"

# 5. Print a welcome message
# tell the user this is a password generator

# 6. Ask the user:
# How many letters would you like in your password?

# 7. Ask the user:
# How many symbols would you like?

# 8. Ask the user:
# How many numbers would you like?

# 9. Create an empty list for the password
# this list will store all chosen characters

# 10. Create a loop for letters
# the loop should repeat as many times as the user asked for letters

# 11. Inside the loop, choose one random letter from the letters list

# 12. Add that random letter to the password list

# 13. Create a loop for symbols
# the loop should repeat as many times as the user asked for symbols

# 14. Inside the loop, choose one random symbol from the symbols list

# 15. Add that random symbol to the password list

# 16. Create a loop for numbers
# the loop should repeat as many times as the user asked for numbers

# 17. Inside the loop, choose one random number from the numbers list

# 18. Add that random number to the password list

# 19. Now the password list has all characters
# but the order is too obvious:
# letters first, then symbols, then numbers

# 20. Shuffle the password list
# so the order becomes random

# 21. Create an empty string for the final password

# 22. Loop through every character in the shuffled password list

# 23. Add each character to the final password string

# 24. Print the final password
print(r"""
__        __   _                          _ 
 \ \      / /__| | ___ ___  _ __ ___   ___| |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_|
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)

        PASSWORD GENERATOR

""")
import random

list_of_lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_of_upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n_letters = list_of_upper_letters + list_of_lower_letters
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", "/", "?", "@"]

nr_letters = int(input("How many letters you wont in password? "))
nr_numbers = int(input("How many numbers you wont in password? "))
nr_symbols = int(input("How many symbols you wont in password? "))

password_list = []

for letter in range(nr_letters):
    random_letter = random.choice(n_letters)
    password_list.append(random_letter)
for number in range(nr_numbers):
    random_number = random.choice(numbers)
    password_list.append(random_number)
for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

random.shuffle(password_list)

password = "".join(password_list)
print(f"\nYour generated password is: {password}")
