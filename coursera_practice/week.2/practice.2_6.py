first = int(input())
last = int(input())

if last % (last-first+1) == 0:
    print('YES')
else:
    print('NO')
