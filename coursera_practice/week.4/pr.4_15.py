def evkl(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        return evkl(a-b, b)
    return b


x, y = (int(input()) for i in range(2))
print(evkl(x, y))
