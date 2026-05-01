# Day 01 – Python Basics

## What I practiced today

Today I practiced the first basic Python concepts:

- `print()`
- text / strings
- new lines with `\n`
- comments with `#`
- `input()`
- variables
- `len()`
- variable naming rules
- swapping variable values
- a small Band Name Generator project

---

## print()

`print()` shows something on the screen.

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

## Strings

Text in Python is written inside quotation marks.

```python
print("Hello Simon")
```

---

## Joining text

I can join text together with the `+` sign.

```python
print("Hello " + "Simon")
```

Output:

```text
Hello Simon
```

---

## New line

`\n` creates a new line.

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

## Comments

A comment starts with `#`.

Python ignores comments. They are notes for humans.

```python
# This is a comment
print("Hello")
```

In PyCharm:

```text
Ctrl + /
```

comments or uncomments the selected line.

---

## input()

`input()` asks the user a question and waits for an answer.

```python
name = input("What is your name? ")
print("Hello " + name + "!")
```

Example:

```text
What is your name? Simon
Hello Simon!
```

---

## Variables

A variable stores a value so I can use it later.

```python
name = "Simon"
print(name)
```

A good variable name should be clear.

Good variable names:

```python
name = "Simon"
length = 5
user_name = "Simon"
```

Bad variable names:

```python
x = "Simon"
n = "Simon"
```

A variable name cannot start with a number.

Bad:

```python
1name = "Simon"
```

Good:

```python
name1 = "Simon"
```

---

## len()

`len()` counts how many characters are inside text.

```python
name = "Simon"
length = len(name)
print(length)
```

Output:

```text
5
```

Because `Simon` has 5 characters.

---

## Input + len()

I can combine `input()` and `len()`.

```python
name = input("What is your name? ")
length = len(name)
print(f"Your name has {length} characters.")
```

Example:

```text
What is your name? Simon
Your name has 5 characters.
```

---

## f-strings

An f-string lets me put variables inside text.

```python
name = "Simon"
print(f"Hello {name}")
```

Output:

```text
Hello Simon
```

This is easier to read than joining many strings with `+`.

---

## Swapping values

I practiced swapping two variable values using a temporary variable.

```python
box1 = "apples"
box2 = "bananas"

box3 = box2
box2 = box1
box1 = box3

print(box1, box2)
```

Output:

```text
bananas apples
```

The temporary variable keeps one value safe while the swap happens.

Step by step:

```text
box1 = apples
box2 = bananas

box3 = bananas
box2 = apples
box1 = bananas
```

---

## Mini project – Band Name Generator

I made a small program that asks for a city and pet name, then creates a band name.

```python
print("Welcome to the Band Name Generator")

city = input("What is the name of the city you grew up in? ")
pet = input("What is your pet name? ")

print(f"Your band name could be {city} {pet}")
```

Example:

```text
Welcome to the Band Name Generator
What is the name of the city you grew up in? Ljubljana
What is your pet name? Rex
Your band name could be Ljubljana Rex
```

---

## Mistakes I noticed

Python is very strict with names.

This works:

```python
name = "Simon"
length = len(name)
print(length)
```

This does not work:

```python
name = "Simon"
length = len(nama)
print(length)
```

Because `nama` is not the same as `name`.

Python does not guess what I meant. It only follows exactly what I wrote, like a tiny digital bureaucrat.

---

## My Day 01 takeaway

Today I learned that Python code runs step by step.

Important basics:

- `print()` displays text
- `input()` gets text from the user
- variables store values
- `len()` counts characters
- comments help explain code
- clear variable names make code easier to understand
- f-strings make text with variables cleaner
- Python variable names must be written exactly the same every time


