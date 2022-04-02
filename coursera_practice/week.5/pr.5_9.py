a, b, c, d, e = int(input()), int(input()), \
                int(input()), int(input()), int(input())
k = 0

for i in range(0, 1001):
    if (a * i ** 3 + b * i ** 2 + c * i + d) == 0 and i != e:
        k += 1
print(k)
