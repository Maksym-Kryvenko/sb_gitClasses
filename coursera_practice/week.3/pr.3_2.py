n = float(input())
res = 0

while n >= 1:
    res += 1/(n**2)
    n -= 1

print(res)
