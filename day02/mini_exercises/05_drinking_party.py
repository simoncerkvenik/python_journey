print("Welcome to the PARTY!")
bill = float(input("What is total cost? "))
tip = int(input("What percentage would you like to pay? 10, 15, 20, 25? "))
people = int(input("How many people to split the drinking party ?"))

total_tips = tip / 100 * bill
total_bill = total_tips + bill
total_cost = total_bill / people


print(f"Total bill with tip is $:{total_bill:.2f}.")
print(f"Each person should pay {total_cost:.2f} dollars.")

print(f"Total cost is ${total_bill:.2f} dollars. So each should pay $:{total_cost:.2f}.")
