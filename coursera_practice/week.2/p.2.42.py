n, m = int(input()), int(input())

if m > n:
    max1, max2 = m, n
else:
    max1, max2 = n, m

while n != 0:
    n = int(input())
    if n >= max1:
        max2, max1 = max1, n
    elif n >= max2:
        max2 = n
print(max2)
