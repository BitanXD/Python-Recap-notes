password = input("Enter your password: ")
if len(password) < 6:
    passwordStrength = "Weak"
elif len(password) < 11:
    passwordStrength = "Medium"
elif len(password) > 10:
    passwordStrength = "Strong"

print("Your password is",passwordStrength)