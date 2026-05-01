# Starting values
score = 0
height = 180
winning = True

# User scores one point
score += 1

# Print only the current score
print(score)

# Different ways to print text together with variables

# 1. Using + and str()
print("Your score is " + str(score))

# 2. Using comma
print("Your score is", score)

# 3. Using an f-string
print(f"Your score is {score}, your height is {height}, and your winning status is {winning}")