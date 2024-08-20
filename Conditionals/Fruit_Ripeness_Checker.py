fruit = input("Enter fruit name: ")
fruitColor = input("Enter fruit color: ")

if fruitColor.lower() == "green":
    fruitCondition = "Unripe"
elif fruitColor.lower() == "yellow":
    fruitCondition = "Ripe"
elif fruitColor.lower() == "brown":
    fruitCondition = "Overripe"

print("Your fruit is ", fruitCondition)