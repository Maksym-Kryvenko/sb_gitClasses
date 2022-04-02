n = int(input())
c = 0
summ = 0

while n != 0:
    summ += n
    c += 1
    n = int(input())

print(summ/c)
