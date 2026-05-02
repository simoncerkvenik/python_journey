#  If / Elif / Else Practice
# Exercise: Coffee size price

# Ask the user for coffee size:
# small / medium / large

# If size is "small":
#     print "Price: 2 euros"

# Elif size is "medium":
#     print "Price: 3 euros"

# Elif size is "large":
#     print "Price: 4 euros"

# Else:
#     print "Invalid size"

print("Welcome to the coffee shop.")
mug_size = input("Which mug size would you like? large, medium, small: ")
if mug_size == "large":
    print("That would be: 10€")
elif mug_size == "medium":
    print("That would be: 5€")
elif mug_size == "small":
    print("That would be 3€")
else:
    print("Invalid size")