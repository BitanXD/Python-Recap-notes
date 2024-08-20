validation = True
while validation:
    value = int(input("Enter a number: "))
    if(value >= 0 and value < 11):
        print("Validation is Successfull")
        validation = False
        break
    else:
        print("Validation Failed")