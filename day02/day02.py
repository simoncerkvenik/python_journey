# Group Snack Splitter
#
# Create a small program that helps a group split the cost of snacks.
#
# The program should ask the user:
# 1. How much did the snacks cost?
# 2. How many people are sharing the snacks?
# 3. How much extra delivery cost was added?
#
# Then calculate:
# - the total cost
# - how much each person should pay
#
# Use:
# - input()
# - variables
# - float()
# - int()
# - math operations
# - f-strings
#
# Example idea:
# Snacks cost: 18.50
# Delivery cost: 3.50
# People: 4
#
# Each person should pay: 5.50
print("Welcome to the Group Snack Splitter!")

snack_cost = input("How much did the snacks cost? ")
delivery_cost = input("How much was the delivery cost? ")
people = input("How many people are sharing the snacks? ")

# Convert the inputs to numbers below:
total_cost = int(snack_cost) + int(delivery_cost) / int(people)

# Calculate the total cost below:
print(f"The total cost is: {total_cost}")

# Calculate how much each person should pay below:


# Print the final result below: