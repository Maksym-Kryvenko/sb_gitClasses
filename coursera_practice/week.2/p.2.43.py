n = int(input())
c = 0
n_max = n

while n != 0:
    if n > n_max:
        n_max = n
        c = 1
    elif n == n_max:
        c += 1
    n = int(input())

print(c)
