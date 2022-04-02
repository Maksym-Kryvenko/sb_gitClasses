import math
a, b, c = float(input()), float(input()), float(input())


if a == 0:
    if b != 0:
        print(1, -c / b)
    if b == 0 and c == 0:
        print(3)
    if b == 0 and c != 0:
        print(0)
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
    elif D == 0:
        print(1, -b/(2*a))
    elif D < 0:
        print(0)
