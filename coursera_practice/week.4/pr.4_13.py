def sum_new(a, b):
    if b == 0:
        return a
    else:
        a += 1
        return sum_new(a, b-1)


print(sum_new(int(input()), int(input())))
