n = int(input())
j = 1
count = 0

while j <= n:
    i = 0
    dig1 = ''
    while (j // 10 ** i) != 0:
        dig = (j // 10 ** i) % 10
        i += 1
        dig1 = int(str(dig1) + str(dig))
    if dig1 == j:
        count += 1
    j += 1
print(count)
