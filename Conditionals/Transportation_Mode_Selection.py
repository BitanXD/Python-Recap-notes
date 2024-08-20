distance = int(input("Enter the distance you want to travel in kms: "))
if distance < 3:
    print("You can walk this distance")
elif distance < 16:
    print("You can take a bike for this distance")
elif distance > 15:
    print("You should take a car to travel this distance")