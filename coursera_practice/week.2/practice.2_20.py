k = int(input())

b = k % 3
c = k % 5

if b % 5 == 0:
    print('YES')
elif c % 3 == 0:
    print('YES')
else:
    print('NO')
