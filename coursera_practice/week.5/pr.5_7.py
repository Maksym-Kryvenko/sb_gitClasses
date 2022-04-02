n = int(input())

b = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in range(1, n+1):
    for j in range(i):
        print(b[j], end='')
    print()
