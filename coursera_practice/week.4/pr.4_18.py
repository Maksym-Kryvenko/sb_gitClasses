def c(k, n):
    if k == 0:
        return 1
    elif k == n:
        return 1
    else:
        return c(k, n - 1) + c(k - 1, n - 1)


n = int(input())
k = int(input())
print(c(k, n))
