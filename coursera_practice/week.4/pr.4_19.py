def sum_new():
    a = int(input())
    if a == 0:
        return 0
    else:
        a = a + sum_new()
        return a


print(sum_new())
