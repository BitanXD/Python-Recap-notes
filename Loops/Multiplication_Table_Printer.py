value = int(input("Enter the value:"))
for i in range(1,11):
    if(i == 5):
        continue
    else:
        print(value,"X",i,"=",value*i)