number = int(input("Enter a number to check if it is prime or not: "))
count = 0
for i in range(1,number + 1):
    if(number % i == 0):
        count = count + 1
if count == 2:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")