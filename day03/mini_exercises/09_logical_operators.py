# Logical operators in Python

# and = both conditions must be True
# or  = at least one condition must be True
# not = reverses True / False

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")
else:
    print("You cannot enter.")

# age must be 18 or more
# AND
# has_ticket must be True

age = 16
has_parent = True

if age >= 18 or has_parent:
    print("You can enter.")
else:
    print("You cannot enter.")

# Either age is 18 or more
# OR
# user has a parent

is_banned = False

if not is_banned:
    print("You can enter.")
else:
    print("You are banned.")

# not True   # False
# not False  # True