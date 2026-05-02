# Exercise: Cinema ticket prices

print("Welcome to the cinema!")

loyalty = input("Do you have a loyalty card? (Y/N): ").lower()
age = int(input("What is your age? "))
price = 0 # start price

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

family_photo = input("Do you wound family photo? (Y/N): ").lower()
if family_photo == "y":
    price += 3
print(f"Your total amount is {price} dollars.")

# With loyalty card:
# 0-12 years  -> 6 euros
# 13-18 years -> 7 euros
# 19+ years   -> 8 euros
#
# Without loyalty card:
# 0-12 years  -> 7 euros
# 13-18 years -> 8 euros
# 19+ years   -> 10 euros