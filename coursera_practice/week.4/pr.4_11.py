def recurs(a, n):
    if n == 0:
        return 1
    return a * recurs(a, n-1)


print(recurs(float(input()), int(input())))
