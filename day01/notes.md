# Day 01 - Band Name Generator

## f-string spacing

In an f-string, Python only prints exactly what I write.

If I want a space between two variables, I must add the space myself.

```python
city = "Ljubljana"
pet = "Kaya"

print(f"{city}{pet}") # no space
print(f"{city} {pet}") # with space
```

Example:

```python
city = "Ljubljana"
pet = "Kaya"

print(f"{city}{pet}") # LjubljanaKaya
print(f"{city} {pet}") # Ljubljana Kaya
```

## Summary

Today I learned that f-strings can insert variables into text.
Spaces are not automatic, so I must write them inside the string.
