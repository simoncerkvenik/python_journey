# Day 03 - Nested If Practice
# Exercise: Check if the user can ride and calculate ticket price

# Ask the user for height and age
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

# First check if the user is tall enough
if height >= 120:
    print("You can ride the rollercoaster.")

    # If the user is tall enough, check their age
    if age >= 18:
        print("Adult ticket: 12 euros")
    else:
        print("Child ticket: 7 euros")

# If the user is not tall enough
else:
    print("You are too short to ride.")