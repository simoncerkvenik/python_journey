# Import random

# Create a list with three choices:
# rock, paper, scissors

# Ask the user:
# What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.

# Save the user's choice as an integer

# Make the computer chose a random number between 0 and 2

# Print user's choice

# Print computer's choice
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

choices = ["Rock", "Paper", "Scissors"]


user_choice = (int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")))

computer_choice = random.randint(0,2)
print("You chose:", game_images[user_choice])
print("Computer chose:", game_images[computer_choice])
# 0 beats 2
# 2 beats 1
# 1 beats 0

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 0 and computer_choice == 1:
    print("You lose")