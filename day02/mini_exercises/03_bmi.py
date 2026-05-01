height = 1.80
weight = 110

bmi = weight / height ** 2

print(bmi)        # Prints the full BMI number with decimals

print(int(bmi))   # Converts BMI to an integer by cutting off the decimals

# round() is better because it rounds the number.
# If the decimal part is 0.5 or more, it usually rounds up.

print(round(bmi))     # Rounds BMI to the nearest whole number

print(round(bmi, 2))  # Rounds BMI to 2 decimal places
# The second number decides how many decimal places we keep.