a, b, c = int(input()), int(input()), int(input()),

if a >= b and a >= c:
    if b >= c:
        a, b, c = c, b, a
        print(a, b, c)
    else:
        a, b, c = b, c, a
        print(a, b, c)
elif b >= a and b >= c:
    if a >= c:
        a, b, c = c, a, b
        print(a, b, c)
    else:
        a, b, c = a, c, b
        print(a, b, c)
else:
    if a >= b:
        a, b, c = b, a, c
        print(a, b, c)
    else:
        a, b, c = a, b, c
        print(a, b, c)
