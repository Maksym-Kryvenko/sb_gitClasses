n = int(input())
n_max = n
while n != 0:
    if n > n_max:
        n_max = n
    n = int(input())
print(n_max)
