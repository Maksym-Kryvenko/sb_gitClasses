def hanoi(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        hanoi(n - 1, x, 6 - x - y)
        print(n, x, y)
        hanoi(n - 1, 6 - x - y, y)


hanoi(int(input()), 1, 3)
