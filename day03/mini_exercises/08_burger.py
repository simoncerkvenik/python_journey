print("Welcome to Python Burger House!")

size = input("What size burger do you want? S, M or L: ").lower()
cheese = input("Do you want extra cheese? Y or N: ").lower()
bacon = input("Do you want bacon? Y or N: ").lower()

bill = 0

# todo: work out how much they need to pay based on their burger size choice.
if size == "s":
    bill += 6
elif size == "m":
    bill += 8
elif size == "l":
    bill += 10

# Small burger (S): 6 euros
# Medium burger (M): 8 euros
# Large burger (L): 10 euros


# todo: work out how much to add to their bill based on their extra cheese choice.
if cheese == "y":
    bill += 1
# Extra cheese: +1 euro


# todo: work out how much to add to their bill based on their bacon choice.
if bacon == "y":
    bill += 2
# Bacon: +2 euros


# todo: print their final bill.
print(f"The total cost is: {bill}")
