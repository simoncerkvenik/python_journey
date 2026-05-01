# [0] gets the first character from the text.
print("welcome"[0])
# [-1] gets the last character from the text.
print("welcome"[-1])
# w e l c o m e
# 0 1 2 3 4 5 6
# w  e  l  c  o  m  e
# -7 -6 -5 -4 -3 -2 -1
# Strings are joined together with +.
print("123456" + "78910")
# Numbers are added together with +.
print(123456 + 78910)
# Underscores make big numbers easier to read.
print(2_200_000)
# A float is a number with a decimal point.
print(3.14)
# Boolean has only two values: True or False.
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)

#len(123)  Error: len() does not work on numbers.
len(str(123))  # Converts the number to text, then counts the characters.
# 123      = number / int
# "123"    = text / string
# len()    = counts characters/items, not the value of a number

# type() shows what kind of data something is.

print(type(123))      # int = whole number
print(type("abc"))    # str = text / string
print(type(123.123))  # float = decimal number
print(type(False))    # bool = True or False

# Data type conversion changes one data type into another.

print(int("123"))      # str to int
print(float("3.14"))   # str to float
print(str(123))        # int to str

print(int("1234") + 5678)

a = int("5") / int(2.7)
print(a)