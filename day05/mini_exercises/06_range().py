# =========================
# SUM FROM 1 TO 100
# =========================

# Start total at 0
total = 0

# Loop from 1 to 100
for number in range(1, 101):

    # Add current number to total
    total += number

# Print final total
print(total)


# =========================
# FIZZBUZZ
# =========================

# Loop from 1 to 100
for number in range(1, 101):

    # First check if number is divisible by both 3 and 5
    # This must be first, because Python reads from top to bottom
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # If number is divisible by 3, print Fizz
    elif number % 3 == 0:
        print("Fizz")

    # If number is divisible by 5, print Buzz
    elif number % 5 == 0:
        print("Buzz")

    # Otherwise print the number
    else:
        print(number)