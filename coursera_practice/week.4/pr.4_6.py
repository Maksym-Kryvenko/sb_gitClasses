def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


def result(x, y, xc, yc, r):
    if IsPointInCircle(x, y, xc, yc, r):
        return "YES"
    return "NO"


print(result(float(input()), float(input()),
             float(input()), float(input()),
             float(input())))
