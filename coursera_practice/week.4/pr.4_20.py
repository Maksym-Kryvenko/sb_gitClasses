def sum_new():
    a = int(input())
    if a == 0:
        return print(0)
    sum_new()
    return print(a)


sum_new()
