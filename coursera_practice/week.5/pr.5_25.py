a = list(map(int, input().split()))
i = 1
while i != len(a) // 2 + 1:
    a[i - 1], a[-i] = a[-i], a[i - 1]
    i = i + 1
for i in a:
    print(i, end=" ")
