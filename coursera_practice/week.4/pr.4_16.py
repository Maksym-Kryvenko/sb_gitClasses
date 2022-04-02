def evkl(a, b):
    if a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    elif a > b:
        return a
    else:
        return b
    return evkl(a, b)


def ReduceFraction(n, m):
    return int(n//evkl(n, m)), int(m//evkl(n, m))


print(*ReduceFraction(int(input()), int(input())))
