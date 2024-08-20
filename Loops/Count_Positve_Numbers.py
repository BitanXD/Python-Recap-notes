numbers = [1,2,-3,-4,-1,5,-5,3,-6,-9,1,8]
countPos = 0
for num in numbers:
    if(num > 0):
        countPos+=1
print("Number of Positive Numbers are",countPos)