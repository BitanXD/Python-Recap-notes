def recursive_Factorial(num):
    if num == 0:
        return 1
    else:
        return num * recursive_Factorial(num-1)

print(recursive_Factorial(6))