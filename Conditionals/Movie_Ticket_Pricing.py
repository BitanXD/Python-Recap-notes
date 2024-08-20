age = int(input("Enter your age: "))
weekDay = int(input("Enter week day: "))

if age >= 18:
    price = 12
elif age < 18:
    price = 8

if(weekDay == 3):
    price = price - 2

print("Enter your ticket price is: ", price)