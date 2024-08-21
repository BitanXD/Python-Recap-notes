def sum_all(*args):
    print(args)
#       (1, 2)
#           3
#       (1, 2, 3, 4, 5, 6, 7)
#           28
#       (1, 2, 3, 4, 5, 6, 7, 8, 9)
#           45
    for i in args:
        print(i * 2)
        # 2
        # 4
    return sum(args)

print(sum_all(1,2)) # 3
# print(sum_all(1,2,3,4,5,6,7))
# print(sum_all(1,2,3,4,5,6,7,8,9))