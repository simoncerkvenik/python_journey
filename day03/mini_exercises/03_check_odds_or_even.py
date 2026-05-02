# Day 03 - Odd or Even Practice
# Exercise: Check if a number is odd or even

# % gives the remainder after division
# If number % 2 == 0, the number is even
# If number % 2 != 0, the number is odd

# Ask the user for a number
number = int(input("Write a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")