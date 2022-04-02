c = n = int(input())
x2, x1 = 0, 0
while n != 0:
    if n == c:
        x2 += 1
        if x2 > x1:
            x1 = x2
    else:
        x2, c = 1, n
    n = int(input())
print(x1)
