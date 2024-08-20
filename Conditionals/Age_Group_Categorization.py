age = input("Enter your age: ")
age = int(age)
if age < 13 :
    print("Child")
elif age >= 13 and age < 20:
    print("Teenager")
elif age >=20 and age < 60:
    print("Adult")
elif age >= 60:
    print("Senior")