# A variable stores a value so we can use it later.

name = input("What is your name? ")
print(name)

name = "Jack"
print(name)

name = "Simon"
print(len(name))

# len() counts how many characters are inside the text.
print(len(input("what is your name? ")))
name = input("What is your name? ")
length = len(name)
print(f"Your name have {length} characters")
# Variable names should be clear and should not contain spaces.
# Use underscores for longer names.
# Good names help us understand the code even months later.
# Bad: l, m, x
# Good: length, message, username, temporary_box
# Variable names cannot start with a number.
# Good: name_length, length1
# Bad: 1length