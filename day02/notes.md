# Day 02 - Python Basics

Day 02 was about basic Python data types, mathematical operations, type conversion, rounding numbers, and using f-strings.

## Topics covered

- Strings
- Indexing
- Integers
- Floats
- Booleans
- Type checking with `type()`
- Type conversion
- Mathematical operations
- Rounding numbers
- F-strings
- Mini exercises

---

## Files

```text
day02/
├── day02.py
└── mini_exercises/
    ├── 01_numbers.py
    ├── 02_mathematical_operations.py
    ├── 03_bmi.py
    ├── 04_score_increment.py
    └── drinking_party.py
```

---

# 1. Strings and indexing

Strings are text values.

```python
print("welcome"[0])
print("welcome"[-1])
```

Output:

```text
w
e
```

## Positive indexes

```text
w e l c o m e
0 1 2 3 4 5 6
```

## Negative indexes

```text
w e l c o m e
-7 -6 -5 -4 -3 -2 -1
```

`[0]` gets the first character.  
`[-1]` gets the last character.

---

# 2. Strings and numbers

Strings are joined together with `+`.

```python
print("123456" + "78910")
```

Output:

```text
12345678910
```

Numbers are added together with `+`.

```python
print(123456 + 78910)
```

Output:

```text
202366
```

---

# 3. Large numbers

Underscores can make large numbers easier to read.

```python
print(2_200_000)
```

Output:

```text
2200000
```

Python ignores the underscores in numbers.

---

# 4. Floats

A float is a number with a decimal point.

```python
print(3.14)
```

Examples:

```python
height = 1.80
weight = 110
price = 12.99
```

---

# 5. Booleans

A boolean can only be `True` or `False`.

```python
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
```

Output:

```text
True
False
```

---

# 6. Type checking

`type()` shows what kind of data something is.

```python
print(type(123))
print(type("abc"))
print(type(123.123))
print(type(False))
```

Output:

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

Meaning:

```text
int = whole number
str = text / string
float = decimal number
bool = True or False
```

---

# 7. Type conversion

Type conversion changes one data type into another.

```python
print(int("123"))
print(float("3.14"))
print(str(123))
```

Examples:

```python
number = int("123")
decimal = float("3.14")
text = str(123)
```

Important:

```python
len(123)
```

This gives an error because `len()` does not work on numbers.

Correct version:

```python
len(str(123))
```

---

# 8. Mathematical operations

```python
# + adds numbers
# - subtracts numbers
# * multiplies numbers
# / divides numbers
# // divides and removes the decimal part
# % gives the remainder
# ** raises a number to a power
```

Examples:

```python
print(10 + 5) # addition
print(10 - 5) # subtraction
print(10 * 5) # multiplication
print(10 / 5) # division
print(10 // 3) # floor division
print(10 % 3) # modulo
print(2 ** 3) # exponent
```

---

# 9. BMI calculator

```python
height = 1.80
weight = 110

bmi = weight / height ** 2

print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))
```

## Notes

```python
print(bmi)
```

Prints the full BMI number with decimals.

```python
print(int(bmi))
```

Converts BMI to an integer by cutting off the decimal part.

```python
print(round(bmi))
```

Rounds BMI to the nearest whole number.

```python
print(round(bmi, 2))
```

Rounds BMI to 2 decimal places.

---

# 10. Rounding

`round()` rounds a number.

```python
number = 33.8

print(round(number))
```

Output:

```text
34
```

Example with 2 decimal places:

```python
number = 3.14159

print(round(number, 2))
```

Output:

```text
3.14
```

---

# 11. F-strings

F-strings allow variables inside text.

```python
score = 0
height = 180
winning = True

score += 1

print(f"Your score is {score}, your height is {height} and your winning status is {winning}")
```

Output:

```text
Your score is 1, your height is 180 and your winning status is True
```

---

# 12. Score increment

```python
score = 0

score += 1

print(score)
```

Output:

```text
1
```

Meaning:

```python
score += 1
```

is the same as:

```python
score = score + 1
```

---

# 13. Formatting decimal numbers

`.2f` prints a float with 2 decimal places.

```python
price = 12.5

print(f"{price:.2f}")
```

Output:

```text
12.50
```

Example:

```python
number = 3.14159

print(f"{number:.2f}")
```

Output:

```text
3.14
```

---

# 14. Drinking party calculator

This mini program calculates:

- total bill with tip
- amount each person should pay

```python
print("Welcome to the PARTY!")

bill = float(input("What is total cost? "))
tip = int(input("What percentage would you like to pay? 10, 15, 20, 25? "))
people = int(input("How many people to split the drinking party? "))

total_tips = tip / 100 * bill
total_bill = total_tips + bill
total_cost = total_bill / people

print(f"Total bill with tip is ${total_bill:.2f}.")
print(f"Each person should pay {total_cost:.2f} dollars.")

print(f"Total cost is ${total_bill:.2f} dollars. So each should pay ${total_cost:.2f}.")
```

Example:

```text
What is total cost? 125.52
What percentage would you like to pay? 25
How many people to split the drinking party? 4
```

Calculation:

```text
125.52 + 25% = 156.90
156.90 / 4 = 39.225
```

Output:

```text
Total bill with tip is $156.90.
Each person should pay 39.23 dollars.
```

---

# 15. Important Day 02 notes

## `input()`

`input()` always gives back text.

```python
age = input("How old are you? ")
```

If we need a number, we convert it:

```python
age = int(input("How old are you? "))
```

## `float()`

Use `float()` for decimal numbers.

```python
bill = float(input("What is total cost? "))
```

## `int()`

Use `int()` for whole numbers.

```python
people = int(input("How many people? "))
```

## `.2f`

Use `.2f` when printing money or numbers with 2 decimals.

```python
print(f"${total_cost:.2f}")
```

---

# Day 02 summary

Today I practiced basic Python data types, math operations, conversion between types, rounding numbers, and using f-strings.

I also built small exercises:

- numbers and data types
- mathematical operations
- BMI calculator
- score increment
- drinking party bill splitter

Day 02 completed.