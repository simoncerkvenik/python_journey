import random

dice = random.randint(1, 6)

print(f"You rolled a {dice}")
if dice == 6:
    print("You can get out")
else:
    print("You need to wait")