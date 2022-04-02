X, Y = int(input()), int(input())
day = 1

while X < Y:
    X += 0.1 * X
    day += 1
print(day)
