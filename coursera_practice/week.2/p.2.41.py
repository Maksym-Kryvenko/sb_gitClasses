n = int(input())
c = 0
n_prev = n

while n != 0:
    if n > n_prev:
        c += 1
    n_prev = n
    n = int(input())

print(c)
