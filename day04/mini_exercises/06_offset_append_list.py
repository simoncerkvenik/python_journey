# OFFSET
# Offset means position or distance from the start.
# In a file, it tells us where we are reading or writing.
# Example: seek(0) moves to the beginning of the file.


# APPEND
# Append means adding something to the end.
# With a list, append() adds a new item to the end of the list.
# With a file, mode "a" adds new text to the end of the file.


# LIST
# A list is a collection of multiple values in one variable.
# We can add, read, change, sort, reverse, or remove items from a list.


# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

print("Original list:")
print(fruits)


# APPEND
# append() adds a new item to the end of the list
fruits.append("orange")
fruits.append("mango")

print("\nAfter append():")
print(fruits)


# INSERT
# insert(index, item) adds an item at a specific position
# Index 0 means the first position in the list
fruits.insert(0, "strawberry")

print("\nAfter insert():")
print(fruits)


# REMOVE
# remove(item) removes an item by its value
fruits.remove("strawberry")

print("\nAfter remove():")
print(fruits)


# SORT
# sort() sorts the list alphabetically
fruits.sort()

print("\nAfter sort():")
print(fruits)


# REVERSE
# reverse() reverses the current order of the list
fruits.reverse()

print("\nAfter reverse():")
print(fruits)


# POP
# pop(index) removes an item by its index
# It also returns the removed item
removed_fruit = fruits.pop(1)

print("\nRemoved item with pop(1):")
print(removed_fruit)

print("\nFinal list:")
print(fruits)