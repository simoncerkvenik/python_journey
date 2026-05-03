# Day 04 - Random, Lists, Modules and Rock Paper Scissors

Today I practiced Python basics with the `random` module, lists, list methods, nested lists, importing my own module, and a small Rock Paper Scissors project.

## What I learned

- How to import the `random` module
- How to generate random integers with `random.randint()`
- How to generate random float numbers with `random.random()` and `random.uniform()`
- How to make a simple coin flip program
- How to use `if`, `elif`, and `else`
- How to compare user input with computer input
- How to use list indexes
- How to print ASCII art from a list
- How to shuffle a list with `random.shuffle()`
- How to use `random.seed()` for repeatable random results
- How to choose one random item from a list with `random.choice()`
- How to create and use lists
- How to access list items with indexes
- How to slice lists
- How to add, remove, sort, reverse, and pop list items
- How to work with nested lists
- How to import and use my own Python module
- How to split code into smaller practice files

## Files

### day04.py

Created a Rock Paper Scissors game.

The user chooses:

```text
0 = Rock
1 = Paper
2 = Scissors
```

The computer chooses a random number between `0` and `2`.

```python
import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice = random.randint(0, 2)

print("You chose:")
print(game_images[user_choice])

print("Computer chose:")
print(game_images[computer_choice])
```

Then I used conditions to decide who wins.

```python
if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
else:
    print("You lose")
```

Important logic:

```text
0 beats 2
2 beats 1
1 beats 0
```

That means:

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
```

## Mini exercises

### 01_random.py

Practiced generating random numbers.

```python
import random

random_number = random.randint(1, 10)
print(random_number)

random_float = random.random()
print(random_float)

random_float1 = random.uniform(1, 10) * 10
print(random_float1)
```

### 02_coin_flip.py

Created a simple coin flip program using a random number.

```python
import random

random_number = random.randint(0, 1)

if random_number == 1:
    print("Tails")
else:
    print("Heads")
```

### 03_ludo.py

Created a simple dice example.

```python
import random

dice = random.randint(1, 6)

print(f"You rolled a {dice}")

if dice == 6:
    print("You can get out")
else:
    print("You need to wait")
```

### 04_shuffle.py

Practiced shuffling a list.

```python
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)
```

I also practiced `random.seed()` to make random results repeatable.

```python
random.seed(10)
random.shuffle(cards)
```

### 05_my_module.py

Practiced importing and using my own module.

```python
import my_module

my_module.greet()
print(my_module.favorite_number)
```

### my_module.py

Created my own Python module with a variable and a function.

```python
favorite_number = 4

def greet():
    print("Hello from my_module")
```

### 06_offset_append_list.py

Practiced list methods.

```python
fruits.append("strawberry")
fruits.remove("strawberry")
fruits.sort()
fruits.reverse()
removed_fruit = fruits.pop(1)
```

Important list methods:

- `append()` adds an item to the end of a list
- `remove()` removes an item by value
- `sort()` sorts the list
- `reverse()` reverses the current order
- `pop()` removes an item by index and returns it

### 07_state_of_america.py

Practiced list slicing and checking list length.

```python
print(states_of_america[1:4])
print(states_of_america[:4])
print(len(states_of_america))
```

Important:

```python
states_of_america[1:4]
```

This prints index `1`, `2`, and `3`.

Index `4` is not included.

### 08_who_will_pay_the_bill.py

Created a small program that randomly chooses who pays the bill.

```python
import random

friend_names = ["Simon", "Natasa", "Verica", "Mare", "Nina", "Tine"]

friend_names = random.choice(friend_names)

print(f"Today's name who will pay for dinner is {friend_names}.")
```

I learned that after using `random.choice()`, the variable is no longer a list. It becomes one selected item from the list.

### 09_nested_list.py

Practiced nested lists.

```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
```

A nested list means one list inside another list.

## Key concepts

### Importing a module

```python
import random
```

This lets me use Python's built-in random tools.

### Random integer

```python
random.randint(1, 10)
```

This gives a random whole number between `1` and `10`.

### Random choice

```python
random.choice(friend_names)
```

This chooses one random item from a list.

### Shuffle

```python
random.shuffle(cards)
```

This changes the order of items inside the list.

### List index

```python
fruits[0]
```

This gives the first item from the list.

### List slicing

```python
states_of_america[1:4]
```

This gives items from index `1` up to index `4`, but index `4` is not included.

### Nested list

```python
dirty_dozen = [fruits, vegetables]
```

This creates a list that contains two other lists.

### My own module

```python
import my_module
```

This imports my own Python file so I can use its variables and functions.

## Notes

This day helped me understand how Python can use randomness, how lists store multiple values, and how modules help organize code.

The Rock Paper Scissors project helped me connect several ideas together:

- user input
- random computer choice
- list indexes
- ASCII art
- conditions
- win / lose / draw logic

I also practiced writing small exercises in separate files, which makes the project easier to read and better organized.