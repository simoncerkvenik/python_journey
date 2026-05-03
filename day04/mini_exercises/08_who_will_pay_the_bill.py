import random

# List of friend names
friend_names = ["Simon", "Natasa", "Verica", "Mare", "Nina", "Tine", "Dejan"]

# Choose one random name from the list
# After this line, friend_names is no longer a list.
# It becomes one string, for example "Tine".
friend_names = random.choice(friend_names)

# Print the chosen name
print(f"Today's name who will pay for dinner is {friend_names}.")

# Choose one random letter from the chosen name
# Example: if friend_names is "Tine", this can print "T", "i", "n", or "e"
print(random.choice(friend_names))


# Create the list again
# We need to do this because friend_names was changed into a string above
friend_names = ["Simon", "Natasa", "Verica", "Mare", "Nina", "Tine", "Dejan"]

# Choose a random index number from 0 to 6
# 0 is the first item in the list
# 6 is the last item in this list
random_index = random.randint(0, 6)

# Print the friend name at the random index
print(friend_names[random_index])