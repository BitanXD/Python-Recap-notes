coffeeSize = input("Enter the coffee size you want: ")
isExtraShot = input("Enter y or n for an Extra Shot of Espresso: ")

if coffeeSize.lower() == "small":
    order = "Small"
elif coffeeSize.lower() == "medium":
    order = "Medium"
elif coffeeSize.lower() == "large":
    order = "Large"

if isExtraShot.lower() == "y":
    print("Your order is",order,"coffee with extra shot of espresso")
else:
    print("Your order is",order,"coffee")