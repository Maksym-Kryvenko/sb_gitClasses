m = int(input())
n = int(input())
k = int(input())

if k < n*m:
    if k % n == 0 or k % m == 0:
        print("YES")
    else:
        print('NO')
else:
    print('NO')
