def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
# yield store the function and state in the memory and returns the value whenever it is called
for num in even_generator(10):
    print(num)