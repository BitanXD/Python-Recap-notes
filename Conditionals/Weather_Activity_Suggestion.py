weatherType = input("Enter current Weather type: ")
if weatherType.lower() == "sunny":
    activity = "Go for a walk"
elif weatherType.lower() == "rainy":
    activity = "Read a book"
elif weatherType.lower() == "snowy":
    activity = "Build a snowman"

print("Since it is",weatherType.lower(),"you can",activity.lower())