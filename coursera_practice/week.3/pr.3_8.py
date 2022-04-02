n = int(input())
x = float(input())
i = 0
sum = 0
while i < n:
    a = float(input())
    sum = (sum + a) * x
    i += 1
a = float(input())
print('{0:.6f}'.format(sum + a))
