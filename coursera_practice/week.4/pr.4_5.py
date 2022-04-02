def IsPointInSquare(x, y):
    return abs(x), abs(y)


def result(x, y):
    if sum(IsPointInSquare(x, y)) <= 1:
        return "YES"
    return "NO"


print(result(float(input()), float(input())))
