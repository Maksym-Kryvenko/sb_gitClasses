N = int(input())
b = 1
c = 0

while b <= N:
    if b == N:
        print('YES')
        c = 1
        break
    b *= 2
if c != 1:
    print('NO')
