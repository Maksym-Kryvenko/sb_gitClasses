n = int(input())
a = 10 ** n
b = a // 10
for i in range(a - 1, b - 1, -2):
    print(i, end=' ')
