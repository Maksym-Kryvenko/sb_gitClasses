n = int(input())

f1, f2 = 0, 1

while n:
    f1, f2 = f2, f1 + f2
    n -= 1

print(f1)
