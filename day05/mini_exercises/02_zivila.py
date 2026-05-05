# =========================
# FRUITS LIST
# =========================

# List of fruits
fruits = [
    "apple", "banana", "orange", "strawberry", "grape",
    "kiwi", "mango", "pineapple", "pear", "peach",
    "plum", "cherry", "watermelon", "melon", "lemon",
    "lime", "blueberry", "raspberry", "blackberry", "apricot"
]

# Loop through every fruit in the list
for fruit in fruits:
    # Print only the fruit name
    print(fruit)

    # Add "pie" to the fruit using +
    print(fruit + "pie")

    # Add text with f-string
    print(f"{fruit} with pie is {fruit}pie")

    # Empty line between fruits
    print()

# Print the whole list once
print(fruits)


# =========================
# STUDENTS AND SCORES - LIST
# =========================

# List of students
students = ["Simon", "Nina", "Mare", "Tine", "Dejan", "Ana", "Luka", "Maja"]

# List of scores
student_scores = [88, 92, 75, 64, 97, 83, 71, 90]

# Calculate total score with built-in sum()
total_exam_score = sum(student_scores)

# Print total score
print(total_exam_score)


# =========================
# STUDENTS AND SCORES - DICTIONARY
# =========================

# Dictionary with student names and their scores
student_scores = {
    "Simon": 88,
    "Nina": 92,
    "Mare": 75,
    "Tine": 64,
    "Dejan": 97,
    "Ana": 83,
    "Luka": 71,
    "Maja": 90
}

# Loop through dictionary items
for student, score in student_scores.items():
    # Print student name and score
    print(f"{student}: {score}")

# Calculate total score from dictionary values
total_exam_score = sum(student_scores.values())

# Print total score
print(f"Total score: {total_exam_score}")


# =========================
# MANUAL SUM WITHOUT sum()
# =========================

# List of scores
student_scores = [88, 92, 75, 64, 97, 83, 71, 90]

# Start total at 0
manual_total = 0

# Loop through every score
for score in student_scores:
    # Add current score to manual_total
    manual_total += score

# Print final total
print(manual_total)