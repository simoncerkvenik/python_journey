# ---------------------------------
# FOR LOOPS IN PYTHON - SHORT NOTES
# ---------------------------------

# A for loop repeats code for every item in something.
# It can loop through:
# - list
# - string
# - range()
# - other collections


# ---------------------------------
# 1. FOR LOOP WITH A LIST
# ---------------------------------

fruits = ["apple", "banana", "kiwi"]

for fruit in fruits:
    print(fruit)

# Logic:
# fruit = "apple"  -> print
# fruit = "banana" -> print
# fruit = "kiwi"   -> print
# stop


# ---------------------------------
# 2. VARIABLE NAME
# ---------------------------------

# fruit is just a temporary variable.
# You can name it anything, but good names help.

for item in fruits:
    print(item)

# item = one value at a time from the list


# ---------------------------------
# 3. range()
# ---------------------------------

for number in range(5):
    print(number)

# range(5) means:
# 0, 1, 2, 3, 4
# It stops before 5.


for number in range(1, 6):
    print(number)

# range(1, 6) means:
# 1, 2, 3, 4, 5


for number in range(0, 10, 2):
    print(number)

# range(0, 10, 2) means:
# 0, 2, 4, 6, 8


# ---------------------------------
# 4. LOOP THROUGH A STRING
# ---------------------------------

word = "Python"

for letter in word:
    print(letter)

# P
# y
# t
# h
# o
# n


# ---------------------------------
# 5. FOR LOOP WITH IF
# ---------------------------------

fruits = ["apple", "banana", "kiwi", "orange"]

for fruit in fruits:
    if fruit == "banana":
        print("I found banana!")
    else:
        print("Not banana:", fruit)

# The loop checks every item.


# ---------------------------------
# 6. ADD ITEMS TO ANOTHER LIST
# ---------------------------------

shopping_cart = []

for fruit in fruits:
    shopping_cart.append(fruit)

print(shopping_cart)

# append() adds one item to the end of a list.


# ---------------------------------
# 7. RANDOM CHOICE IN FOR LOOP
# ---------------------------------

import random

shopping_cart = []

for item in range(3):
    random_fruit = random.choice(fruits)
    shopping_cart.append(random_fruit)

print(shopping_cart)

# Problem:
# random.choice() can pick the same fruit again.
# Example:
# ["banana", "banana", "kiwi"]


# ---------------------------------
# 8. RANDOM WITHOUT DUPLICATES - WHILE IS BETTER
# ---------------------------------

shopping_cart = []

while len(shopping_cart) < 3:
    random_fruit = random.choice(fruits)

    if random_fruit not in shopping_cart:
        shopping_cart.append(random_fruit)

print(shopping_cart)

# while repeats until shopping_cart has 3 different fruits.


# ---------------------------------
# 9. break
# ---------------------------------

for fruit in fruits:
    if fruit == "kiwi":
        print("Kiwi found!")
        break

    print(fruit)

# break stops the loop immediately.


# ---------------------------------
# 10. continue
# ---------------------------------

for fruit in fruits:
    if fruit == "banana":
        continue

    print(fruit)

# continue skips the current loop round.


# ---------------------------------
# 11. enumerate()
# ---------------------------------

for index, fruit in enumerate(fruits):
    print(index, fruit)

# enumerate() gives:
# index + item


# ---------------------------------
# 12. TOTAL
# ---------------------------------

numbers = [5, 10, 15]

total = 0

for number in numbers:
    total += number

print(total)

# total = 0 + 5 + 10 + 15
# result = 30


# ---------------------------------
# 13. BIGGEST NUMBER
# ---------------------------------

numbers = [4, 9, 2, 20, 7]

biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print(biggest)

# Check every number.
# If number is bigger than biggest, replace biggest.


# ---------------------------------
# 14. NESTED FOR LOOP
# ---------------------------------

tools = ["hammer", "saw"]
materials = ["wood", "metal"]

for tool in tools:
    for material in materials:
        print(tool, material)

# loop inside another loop


# ---------------------------------
# 15. COMMON MISTAKES
# ---------------------------------

# Correct:
for fruit in fruits:
    print(fruit)

# Wrong:
# for fruit in fruits
#     print(fruit)
# Missing colon :

# Wrong:
# for fruit in fruits:
# print(fruit)
# Missing indentation


# ---------------------------------
# 16. FOR VS WHILE
# ---------------------------------

# for = loop through known things
# Example:
# every item in a list
# every number in range()
# every letter in a word

# while = repeat while condition is True
# Example:
# while cart is not full
# while password is wrong
# while game is running