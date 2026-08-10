name = input("Enter student's name: ")
score = float(input("Enter student's score: "))

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 45:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Score:", score)
print("Grade:", grade)