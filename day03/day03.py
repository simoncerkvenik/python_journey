from random import choice

print(r""" 
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
""")

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input("Left or Right.").lower()
if choice1 == "right":
    print("Game over.!")
elif choice1 == "left":
    choice2 = input("swim or wait:").lower()
    if choice2 == "swim":
        print("You die by alligator!")
    elif choice2 == "wait":
        choice3 = input("Which door: red, blue or yellow")
    if choice3 == "red":
        print("Burned by fire. Game Over")
    elif choice3 == "blue":
        print("Eaten by beasts. Game Over")
    elif choice3 == "yellow":
        print("Well done. You win")
    else:
        print("Game Over")
