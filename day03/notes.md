# Day 03 - Control Flow and Logical Operators

Day 03 was about making decisions in Python.

Main topics:

- `if`
- `else`
- `elif`
- comparison operators
- nested `if`
- modulo `%`
- logical operators
- raw strings for ASCII art
- small decision-based programs

---

## Files

```text
day03/
├── day03.py
├── notes.md
└── mini_exercises/
    ├── 01_if_else.py
    ├── 02_swiming_pool_entry.py
    ├── 03_check_odds_or_even.py
    ├── 04_nested_if_statement.py
    ├── 05_access.py
    ├── 06_if_elif_else.py
    ├── 07_cinema.py
    ├── 08_burger.py
    └── 09_logical_operators.py
```

---

# 1. If / else

`if` checks if something is true.

```python
age = int(input("What is your age? "))

if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote!")
```

## Logic

```text
if condition is True:
    run this code
else:
    run this other code
```

The code under `if` and `else` must be indented.

---

# 2. Indentation

Python uses indentation to understand which code belongs where.

Correct:

```python
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
```

Wrong:

```python
if age >= 18:
print("You are an adult.")
```

This is wrong because the `print()` line is not indented.

---

# 3. Comparison operators

Comparison operators compare values.

```python
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
```

Examples:

```python
age = 18

if age == 18:
    print("You are 18.")

if age != 18:
    print("You are not 18.")

if age > 18:
    print("You are older than 18.")

if age < 18:
    print("You are younger than 18.")

if age >= 18:
    print("You are an adult.")

if age <= 18:
    print("You are 18 or younger.")
```

Important:

```python
age = 18
```

means assign value.

```python
age == 18
```

means compare value.

---

# 4. Swimming pool entry

Mini exercise: check if the user can enter the swimming pool alone.

```python
# Day 03 - If Practice
# Exercise: Check if the user can enter the swimming pool

age = int(input("How old are you? "))

if age >= 12:
    print("You can enter the swimming pool alone.")
else:
    print("You need an adult with you.")
```

## Logic

```text
If age is 12 or more:
    user can enter alone
Otherwise:
    user needs an adult
```

---

# 5. Modulo %

Modulo gives the remainder after division.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 / 3 = 3 remainder 1
```

Modulo is useful for checking if a number is even or odd.

---

# 6. Odd or even checker

```python
# Day 03 - Odd or Even Practice
# Exercise: Check if a number is odd or even

number = int(input("Write a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

## Logic

```text
If number % 2 == 0:
    number is even
Otherwise:
    number is odd
```

Examples:

```text
4 % 2 = 0 -> even
5 % 2 = 1 -> odd
```

---

# 7. Nested if

Nested `if` means an `if` statement inside another `if` statement.

```python
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster.")

    if age >= 18:
        print("Adult ticket: 12 euros")
    else:
        print("Child ticket: 7 euros")
else:
    print("You are too short to ride.")
```

## Logic

```text
First check height.

If height is enough:
    check age
    if adult:
        adult ticket
    else:
        child ticket
else:
    too short
```

---

# 8. Password access with nested if

```python
# Mini Exercise - Nested If
# Goal: Practice an if statement inside another if statement

pass_access = "simon"

print("Welcome to the vault!")

password = input("Please enter your password: ")

if password == pass_access:
    age = int(input("Please enter your age: "))

    if age >= 18:
        print("Access granted.")
    else:
        print("You are too young.")
else:
    print("Wrong password.")
```

## Logic

```text
First check password.

If password is correct:
    ask for age
    if age is 18 or more:
        access granted
    else:
        too young
else:
    wrong password
```

---

# 9. If / elif / else

Use `elif` when there are more than two possible choices.

```python
mug_size = input("Which mug size would you like? large, medium, small: ")

if mug_size == "large":
    print("That would be: 10€")
elif mug_size == "medium":
    print("That would be: 5€")
elif mug_size == "small":
    print("That would be: 3€")
else:
    print("Invalid size")
```

## Logic

```text
if first condition is true:
    run this
elif second condition is true:
    run this
elif third condition is true:
    run this
else:
    invalid choice
```

---

# 10. Cinema ticket calculator

This exercise calculates ticket price based on:

- loyalty card
- age
- family photo

```python
print("Welcome to the cinema!")

loyalty = input("Do you have loyalty? (Y/N): ").lower()
age = int(input("What is your age? "))

price = 0

if loyalty == "y":
    if age <= 12:
        price = 6
    elif age <= 18:
        price = 7
    else:
        price = 8
else:
    if age <= 12:
        price = 7
    elif age <= 18:
        price = 8
    else:
        price = 10

family_photo = input("Do you want family photo? (Y/N): ").lower()

if family_photo == "y":
    price += 3

print(f"Your total amount is {price} dollars.")
```

## Price table

With loyalty card:

```text
0-12 years -> 6 euros
13-18 years -> 7 euros
19+ years -> 8 euros
```

Without loyalty card:

```text
0-12 years -> 7 euros
13-18 years -> 8 euros
19+ years -> 10 euros
```

Family photo:

```text
+3 euros
```

Important lesson:

```python
print("Ticket price: 8 euros")
```

only prints text.

```python
price = 8
```

saves the value into a variable.

Računalnik ne bere misli, grozno, vem.

---

# 11. Burger calculator

```python
print("Welcome to Python Burger House!")

size = input("What size burger do you want? S, M or L: ").lower()
cheese = input("Do you want extra cheese? Y or N: ").lower()
bacon = input("Do you want bacon? Y or N: ").lower()

bill = 0

if size == "s":
    bill += 6
elif size == "m":
    bill += 8
elif size == "l":
    bill += 10

if cheese == "y":
    bill += 1

if bacon == "y":
    bill += 2

print(f"The total cost is: {bill}")
```

## Prices

```text
Small burger -> 6 euros
Medium burger -> 8 euros
Large burger -> 10 euros
Extra cheese -> +1 euro
Bacon -> +2 euros
```

## Important

These checks are separate:

```python
if cheese == "y":
    bill += 1

if bacon == "y":
    bill += 2
```

Because the user can choose both cheese and bacon.

---

# 12. Logical operators

Logical operators combine conditions.

```python
and
or
not
```

---

## and

Both conditions must be true.

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")
else:
    print("You cannot enter.")
```

Logic:

```text
age must be 18 or more
AND
has_ticket must be True
```

---

## or

Only one condition needs to be true.

```python
age = 16
has_parent = True

if age >= 18 or has_parent:
    print("You can enter.")
else:
    print("You cannot enter.")
```

Logic:

```text
Either age is 18 or more
OR
user has a parent
```

---

## not

`not` flips the boolean value.

```python
is_banned = False

if not is_banned:
    print("You can enter.")
else:
    print("You are banned.")
```

Meaning:

```text
not True -> False
not False -> True
```

---

# 13. Treasure Island game

This project uses multiple `if`, `elif`, and `else` statements.

```python
print(r"""
        ___________
       / /|
      /__________/ |
      | TREASURE | |
      | $$$$$ | |
      |__________|/
""")

print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("Left or Right: ").lower()

if choice1 == "right":
    print("Game over.")
elif choice1 == "left":
    choice2 = input("Swim or wait: ").lower()

    if choice2 == "swim":
        print("You die by alligator!")
    elif choice2 == "wait":
        choice3 = input("Which door: red, blue or yellow: ").lower()

        if choice3 == "red":
            print("Burned by fire. Game Over")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over")
        elif choice3 == "yellow":
            print("Well done. You win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
```

---

# 14. ASCII art in Python

ASCII art can be printed with triple quotes.

```python
print("""
ASCII ART HERE
""")
```

If the ASCII art contains backslashes `\`, use raw string:

```python
print(r"""
\ / \ /
 \/ \/
""")
```

The `r` means raw string.

It tells Python:

```text
Do not treat \ as a special escape character.
```

Without `r`, Python may treat `\n`, `\t`, and other combinations as special characters.

---

# 15. Important Day 03 notes

## input() gives text

```python
age = input("What is your age? ")
```

This gives text.

For numbers, convert it:

```python
age = int(input("What is your age? "))
```

---

## lower()

`.lower()` makes input lowercase.

```python
choice = input("Left or Right: ").lower()
```

This helps because:

```text
LEFT
Left
left
```

all become:

```text
left
```

---

## +=

```python
bill += 2
```

means:

```python
bill = bill + 2
```

Example:

```python
bill = 10
bill += 2

print(bill)
```

Output:

```text
12
```

---

## if / elif / else order

Python checks from top to bottom.

```python
if condition1:
    run this
elif condition2:
    run this
else:
    run this
```

When one condition is true, Python does that block and skips the rest.

---

# Day 03 summary

Today I practiced decision making in Python.

I used:

- `if`
- `else`
- `elif`
- nested `if`
- comparison operators
- modulo `%`
- logical operators
- `.lower()`
- `+=`
- raw strings for ASCII art

I built small programs:

- voting age checker
- swimming pool entry checker
- odd or even checker
- rollercoaster ticket checker
- password access checker
- coffee size price checker
- cinema ticket calculator
- burger calculator
- logical operators examples
- Treasure Island game

Day 03 completed.