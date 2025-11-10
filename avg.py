# student_grade.py

# Marks for 5 subjects (predefined, since user input is not allowed)
marks = [85, 78, 92, 67, 74]  # you can change these values

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 85:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 55:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Print the results
print(f"Marks: {marks}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
