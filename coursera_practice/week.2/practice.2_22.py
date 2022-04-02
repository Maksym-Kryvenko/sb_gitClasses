k = int(input())
m = int(input())
n = int(input())

if n % k == 0:
    print(m*2*(n//k))

elif n % k != 0:
    print(m*2*(n//k)+m*2)
