score = int(input("Enter marks obtained: "))
if score < 60:
    grade = "F"
elif score < 70:
    grade = "D"
elif score < 80:
    grade = "C"
elif score < 90:
    grade = "B"
elif score <= 100:
    grade = "A"

print("Your grade is : ", grade)