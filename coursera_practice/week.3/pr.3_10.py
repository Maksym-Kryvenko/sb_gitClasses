import math
a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif D == 0:
    print(-b/(2*a))
else:
    pass
